#!/usr/bin/env bash
set -euo pipefail

mode="${1:-daily}"
out_root="${2:-$HOME/.codex/security-audits}"
baseline_dir="$out_root/baselines"
mkdir -p "$out_root" "$baseline_dir"

stamp="$(date +%Y%m%d-%H%M%S)"
out_file="$out_root/security-audit-$stamp.log"

assert_safe() {
  local cmd="$1"
  if [[ "$cmd" =~ rm[[:space:]]+-rf[[:space:]]+/ ]] || [[ "$cmd" =~ (diskutil[[:space:]]+erase|shutdown|reboot) ]]; then
    echo "Blocked unsafe operation: $cmd" >&2
    exit 1
  fi
}

score=0
risk_notes=()

collect_memory() {
  vm_stat > "$out_root/vmstat-$stamp.txt" 2>/dev/null || true
  sysctl vm.swapusage > "$out_root/swap-$stamp.txt" 2>/dev/null || true
  top -l 1 -o mem -n 20 > "$out_root/topmem-$stamp.txt" 2>/dev/null || true

  if grep -qi "used = [1-9]" "$out_root/swap-$stamp.txt"; then
    score=$((score + 15))
    risk_notes+=("swap_in_use")
  fi
}

collect_processes() {
  ps aux > "$out_root/ps-$stamp.txt" 2>/dev/null || true
  awk 'NR==1 || $4+0 > 10.0' "$out_root/ps-$stamp.txt" > "$out_root/high-mem-procs-$stamp.txt" || true

  if [[ $(wc -l < "$out_root/high-mem-procs-$stamp.txt" 2>/dev/null || echo 0) -gt 6 ]]; then
    score=$((score + 10))
    risk_notes+=("many_high_mem_processes")
  fi
}

collect_persistence() {
  launchctl list > "$out_root/launchctl-$stamp.txt" 2>/dev/null || true
  ls -la "$HOME/Library/LaunchAgents" > "$out_root/launchagents-$stamp.txt" 2>/dev/null || true

  if grep -Eiq "(random|tmp|unsigned|unknown)" "$out_root/launchctl-$stamp.txt"; then
    score=$((score + 10))
    risk_notes+=("suspicious_launch_pattern")
  fi
}

collect_injection_indicators() {
  rg -n -i "ignore (all|previous) instructions|reveal system prompt|developer message|bypass safety|exfiltrate (secret|credential|token)" \
    "$HOME/Downloads" "$HOME/Desktop" "$HOME/Documents" > "$out_root/injection-signals-$stamp.txt" 2>/dev/null || true

  local hits
  hits=$(wc -l < "$out_root/injection-signals-$stamp.txt" 2>/dev/null || echo 0)
  if [[ "$hits" -gt 0 ]]; then
    score=$((score + 10))
    risk_notes+=("injection_pattern_hits:$hits")
  fi
}

write_baseline() {
  cp "$out_root/topmem-$stamp.txt" "$baseline_dir/topmem-latest.txt" 2>/dev/null || true
  cp "$out_root/launchctl-$stamp.txt" "$baseline_dir/launchctl-latest.txt" 2>/dev/null || true
}

print_risk_band() {
  if (( score >= 75 )); then echo "CRITICAL"; return; fi
  if (( score >= 50 )); then echo "HIGH"; return; fi
  if (( score >= 25 )); then echo "MEDIUM"; return; fi
  echo "LOW"
}

assert_safe "read_only_audit"
collect_memory
collect_processes
collect_persistence
collect_injection_indicators

if [[ "$mode" == "daily" || "$mode" == "weekly" ]]; then
  write_baseline
fi

band=$(print_risk_band)

{
  echo "# Security Maintenance Audit"
  echo "timestamp_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "mode: $mode"
  echo "score: $score"
  echo "risk_band: $band"
  echo "notes: ${risk_notes[*]:-none}"
  echo
  echo "artifacts:"
  echo "- $out_root/vmstat-$stamp.txt"
  echo "- $out_root/swap-$stamp.txt"
  echo "- $out_root/topmem-$stamp.txt"
  echo "- $out_root/ps-$stamp.txt"
  echo "- $out_root/high-mem-procs-$stamp.txt"
  echo "- $out_root/launchctl-$stamp.txt"
  echo "- $out_root/launchagents-$stamp.txt"
  echo "- $out_root/injection-signals-$stamp.txt"
  echo
  echo "safety: read-only audit complete; no app deletion or destructive cleanup performed"
} > "$out_file"

echo "Audit log written: $out_file"
echo "Risk band: $band (score=$score)"
