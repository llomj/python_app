import { EditorView, Decoration, DecorationSet } from '@codemirror/view';
import { StateField } from '@codemirror/state';
import { syntaxTree, HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { tags as t } from '@lezer/highlight';

const PYTHON_BUILTINS = new Set([
  'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
  'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod',
  'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'getattr',
  'globals', 'hasattr', 'hash', 'hex', 'id', 'input', 'int', 'isinstance',
  'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview',
  'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
  'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
  'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', '__import__',
]);

const orangeMark = Decoration.mark({ attributes: { style: 'color:#FF9700' } });
const redMark = Decoration.mark({ attributes: { style: 'color:#FF1900' } });

const varHighlightField = StateField.define<DecorationSet>({
  create(state) {
    return computeVarDecorations(state);
  },
  update(deco, tr) {
    if (!tr.docChanged) return deco;
    return computeVarDecorations(tr.state);
  },
  provide: f => EditorView.decorations.from(f),
});

function computeVarDecorations(state) {
  const decos = [];
  syntaxTree(state).iterate({
    enter(node) {
      if (node.name === 'VariableName') {
        const parent = node.node.parent;
        if (parent && parent.name === 'CallExpression') {
          const name = state.sliceDoc(node.from, node.to);
          if (PYTHON_BUILTINS.has(name)) {
            decos.push(orangeMark.range(node.from, node.to));
          } else {
            decos.push(redMark.range(node.from, node.to));
          }
        } else {
          decos.push(redMark.range(node.from, node.to));
        }
      }
    },
  });
  return Decoration.set(decos);
}

export const editorUiTheme = EditorView.theme({
  "&": {
    backgroundColor: "#050c18 !important",
    fontSize: "14px",
    height: "100%",
    color: "#ffffff"
  },
  ".cm-gutters": {
    backgroundColor: "#050c18 !important",
    color: "#2d4a77",
    border: "none"
  }
}, { dark: true });

export const pythonHighlightStyle = HighlightStyle.define([
  { tag: t.comment, color: "#858585" },
  { tag: t.keyword, color: "#389EDB" },
  { tag: t.number, color: "#FF00FF" },
  { tag: t.string, color: "#00AD89" },
  { tag: t.escape, color: "#00AD89" },
  { tag: t.invalid, color: "#00AD89" },
]);

export const customPythonTheme = [
  editorUiTheme,
  syntaxHighlighting(pythonHighlightStyle),
  varHighlightField,
];
