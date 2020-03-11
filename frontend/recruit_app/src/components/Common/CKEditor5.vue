<template>
  <div id="app">
    <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
  </div>
</template>

<script>
// import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

export default {
  name: "app",
  data() {
    return {
      editor: ClassicEditor,
      editorData: "<p>发个动态，见证当下</p>",
      editorConfig: {
        // The configuration of the editor.
      }
    };
  }
};
</script>

<style lang="less" rel="stylesheet/less">
/*
 * CKEditor 5 (v16.0.0) content styles.
 * Generated on Thu, 13 Feb 2020 14:40:38 GMT.
 * For more information, check out https://ckeditor.com/docs/ckeditor5/latest/builds/guides/integration/content-styles.html
 */

:root {
  --ck-highlight-marker-blue: #72cdfd;
  --ck-highlight-marker-green: #63f963;
  --ck-highlight-marker-pink: #fc7999;
  --ck-highlight-marker-yellow: #fdfd77;
  --ck-highlight-pen-green: #118800;
  --ck-highlight-pen-red: #e91313;
  --ck-image-style-spacing: 1.5em;
  --ck-todo-list-checkmark-size: 16px;
}
.ck-editor__editable {
  min-height: 100px;
}
.ck-content {
  /*!
Misty Light
Brought to you with ❤️ by E-Tiger Studio, 2017-2020
https://github.com/etigerstudio/typora-misty-theme
 */
  a {
    color: #4183c4;
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    position: relative;
    margin-top: 1.8rem;
    margin-bottom: 1rem;
    font-weight: 400;
    line-height: 1.4;
    cursor: text;
    color: #142331;
  }
  h1:hover a.anchor,
  h2:hover a.anchor,
  h3:hover a.anchor,
  h4:hover a.anchor,
  h5:hover a.anchor,
  h6:hover a.anchor {
    text-decoration: none;
  }
  h1 code,
  h1 tt,
  h2 code,
  h2 tt,
  h3 code,
  h3 tt,
  h4 code,
  h4 tt,
  h5 code,
  h5 tt,
  h6 code,
  h6 tt {
    font-size: inherit;
  }
  h1 {
    text-align: center;
    padding-bottom: 0.3em;
    font-size: 2.25em;
    line-height: 1.2;
    margin: 1em auto 1.2em;
    font-weight: 300;
  }
  h1:after {
    border-bottom: 2px dashed #afec9e;
    content: "";
    width: 100px;
    display: block;
    margin: 0.2em auto 0;
    height: 2px;
  }
  h2 {
    font-size: 1.75em;
    padding-left: 9px;
    line-height: 1.4;
    border-left: 6px solid #cce5ff;
  }
  h3 {
    font-size: 1.5em;
    line-height: 1.43;
  }
  h3:before {
    border-radius: 50%;
    background-color: #9ed0ff;
    content: "";
    width: 6px;
    display: inline-block;
    height: 6px;
    vertical-align: middle;
    margin-bottom: 0.18em;
    margin-right: 8px;
  }
  h4 {
    font-size: 1.25em;
  }
  h4:before {
    background-color: #9ed0ff;
    content: "";
    width: 6px;
    display: inline-block;
    height: 2px;
    vertical-align: middle;
    margin-bottom: 0.18em;
    margin-right: 8px;
  }
  h5 {
    font-size: 1em;
  }
  h6 {
    font-size: 1em;
    color: #777;
  }
  blockquote,
  dl,
  ol,
  p,
  table,
  ul {
    margin: 0.8em 0;
  }
  li > ol,
  li > ul {
    margin: 0;
  }
  hr {
    height: 0.25em;
    padding: 0;
    margin: 24px 0;
    background-color: #e1e4e8;
    border: 0;
  }
  a:first-child h1,
  a:first-child h2,
  a:first-child h3,
  a:first-child h4,
  a:first-child h5,
  a:first-child h6,
  body > h1:first-child,
  body > h1:first-child + h2,
  body > h2:first-child,
  body > h3:first-child,
  body > h4:first-child,
  body > h5:first-child,
  body > h6:first-child {
    margin-top: 0;
    padding-top: 0;
  }
  h1 p,
  h2 p,
  h3 p,
  h4 p,
  h5 p,
  h6 p {
    margin-top: 0;
  }
  li p.first {
    display: inline-block;
  }
  ol,
  ul {
    padding-left: 30px;
  }
  ol:first-child,
  ul:first-child {
    margin-top: 0;
  }
  ol:last-child,
  ul:last-child {
    margin-bottom: 0;
  }
  blockquote {
    border-left: 4px dotted #e5e8e8;
    padding: 0 12px;
    color: #444;
    font-size: 0.9em;
  }
  blockquote blockquote {
    padding-right: 0;
  }
  table {
    padding: 0;
    word-break: initial;
  }
  table tr {
    border-top: 1px solid #dadfe6;
    margin: 0;
    padding: 0;
  }
  table.md-table tr:nth-child(2n) {
    background-color: #fafbfc;
  }
  table tr th {
    font-weight: 400;
    border: 1px solid #dadfe6;
    text-align: left;
    margin: 0;
    padding: 6px 13px;
  }
  table tr td {
    border: 1px solid #dadfe6;
    text-align: left;
    margin: 0;
    padding: 6px 13px;
  }
  table tr td:first-child,
  table tr th:first-child {
    margin-top: 0;
  }
  table tr td:last-child,
  table tr th:last-child {
    margin-bottom: 0;
  }
  .CodeMirror-gutters {
    border-right: 1px solid #ddd;
  }
  .md-fences,
  code,
  tt {
    font-size: 90%;
    border-radius: 3px;
    font-family: "SF Mono", Consolas, "Liberation Mono", Menlo, Courier,
      monospace, "PingFang SC", "Microsoft YaHei", "微软雅黑";
  }
  code,
  tt {
    margin: 0 2px;
    padding: 2px 4px;
    background-color: #e2f0ff;
  }
}
</style>