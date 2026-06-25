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

const builtinMark = Decoration.mark({ attributes: { style: 'color:#FF9700' } });

const builtinHighlightField = StateField.define<DecorationSet>({
  create(state) {
    return computeBuiltinDecorations(state);
  },
  update(deco, tr) {
    if (!tr.docChanged) return deco;
    return computeBuiltinDecorations(tr.state);
  },
  provide: f => EditorView.decorations.from(f),
});

function computeBuiltinDecorations(state) {
  const decos = [];
  syntaxTree(state).iterate({
    enter(node) {
      if (node.name === 'CallExpression') {
        const varName = node.node.getChild('VariableName');
        if (varName) {
          const name = state.sliceDoc(varName.from, varName.to);
          if (PYTHON_BUILTINS.has(name)) {
            decos.push(builtinMark.range(varName.from, varName.to));
          }
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
  { tag: t.variableName, color: "#FF1900" },
  { tag: t.name, color: "#ffffff" },
  { tag: t.number, color: "#FF00FF" },
  { tag: t.string, color: "#00AD89" },
]);

export const customPythonTheme = [
  editorUiTheme,
  syntaxHighlighting(pythonHighlightStyle),
  builtinHighlightField,
];
