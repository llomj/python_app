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

export interface EditorColorSettings {
  comment: string;
  identifier: string;
  builtin: string;
  keyword: string;
  number: string;
  string: string;
}

export const DEFAULT_EDITOR_COLORS: EditorColorSettings = {
  comment: "#858585",
  identifier: "#FF1900",
  builtin: "#FF9700",
  keyword: "#389EDB",
  number: "#FF00FF",
  string: "#00AD89",
};

const createVarHighlightField = (colors: EditorColorSettings) => {
  const builtinMark = Decoration.mark({ attributes: { style: `color:${colors.builtin}` } });
  const identifierMark = Decoration.mark({ attributes: { style: `color:${colors.identifier}` } });

  return StateField.define<DecorationSet>({
    create(state) {
      return computeVarDecorations(state, builtinMark, identifierMark);
    },
    update(deco, tr) {
      if (!tr.docChanged) return deco;
      return computeVarDecorations(tr.state, builtinMark, identifierMark);
    },
    provide: f => EditorView.decorations.from(f),
  });
};

function computeVarDecorations(state, builtinMark, identifierMark) {
  const decos = [];
  syntaxTree(state).iterate({
    enter(node) {
      if (node.name === 'VariableName') {
        const parent = node.node.parent;
        if (parent && parent.name === 'CallExpression') {
          const name = state.sliceDoc(node.from, node.to);
          if (PYTHON_BUILTINS.has(name)) {
            decos.push(builtinMark.range(node.from, node.to));
          } else {
            decos.push(identifierMark.range(node.from, node.to));
          }
        } else {
          decos.push(identifierMark.range(node.from, node.to));
        }
      }
    },
  });
  return Decoration.set(decos);
}

export const editorUiTheme = (bgColor: string = "#050c18") => EditorView.theme({
  "&": {
    backgroundColor: `${bgColor} !important`,
    fontSize: "14px",
    height: "100%",
    color: "#ffffff"
  },
  ".cm-gutters": {
    backgroundColor: `${bgColor} !important`,
    color: "#2d4a77",
    border: "none"
  }
}, { dark: true });

export const createPythonHighlightStyle = (colors: EditorColorSettings) => HighlightStyle.define([
  { tag: t.comment, color: colors.comment },
  { tag: t.keyword, color: colors.keyword },
  { tag: t.number, color: colors.number },
  { tag: t.string, color: colors.string },
  { tag: t.escape, color: colors.string },
  { tag: t.invalid, color: colors.string },
]);

export const createCustomPythonTheme = (colors: EditorColorSettings = DEFAULT_EDITOR_COLORS, bgColor?: string) => [
  editorUiTheme(bgColor),
  syntaxHighlighting(createPythonHighlightStyle(colors)),
  createVarHighlightField(colors),
];

export const customPythonTheme = createCustomPythonTheme();
