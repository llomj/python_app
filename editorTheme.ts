import { EditorView } from '@codemirror/view';
import { HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { tags as t } from '@lezer/highlight';
export const editorUiTheme = EditorView.theme({ "&": { backgroundColor: "#050c18 !important", fontSize: "14px", height: "100%", color: "#ffffff" }, ".cm-gutters": { backgroundColor: "#050c18 !important", color: "#2d4a77", border: "none" } }, { dark: true });
export const pythonHighlightStyle = HighlightStyle.define([ { tag: t.comment, color: "#858585" }, { tag: [t.variableName, t.name], color: "#FF1900" }, { tag: t.standard(t.name), color: "#FF9700" }, { tag: t.keyword, color: "#389EDB" }, { tag: t.number, color: "#FF00FF" }, { tag: t.string, color: "#00AD89" } ]);
export const customPythonTheme = [editorUiTheme, syntaxHighlighting(pythonHighlightStyle)];
