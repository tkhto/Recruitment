<template>
  <div class="article">
    <div class="header">
      <span class="avatar">
        <img class="img" :src="userInfo.avatar" />
      </span>
      <div class="user-info">
        <span class="name">{{ userInfo.nic_name }}</span>
        <p class="article-info">
          <span class="pub-date"><i class="el-icon-time"></i> {{ item.update_date | dateStr }}</span>
          <span class="pub-date"><i class="el-icon-view"></i> {{ item.read_num }}</span>
        </p>
      </div>
      <el-dropdown class="more-operate" trigger="hover">
        <span class="el-dropdown-link">
          <i class="fa fa-ellipsis-v"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <li class="el-dropdown-item">
            <a :href="`/editarticle/${item.id}`" target="_blank">
              <i class="el-icon-edit-outline"></i> 修改
            </a>
          </li>
          <li class="el-dropdown-item" @click="removeArticle(item.id)">
            <i class="el-icon-delete"></i> 删除
          </li>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div class="article-header">
      <header class="title"><a :href="`/article/${item.id}`" target="_blank">{{ item.title }}</a></header>
    </div>
    <div class="footer">
      <span>
        <i class="el-icon-chat-line-square"></i> 0
      </span>
      <span>
        <i class="el-icon-star-off"></i> 0
      </span>
    </div>
  </div>
</template>

<script>
import moment from "moment";
export default {
  data() {
    return {};
  },
  props: {
    item: {
      type: Object,
      require: true
    },
    userInfo: {
      type: Object,
      require: true
    }
  },
  filters: {
    dateStr: function(value, format = "YYYY-MM-DD HH:mm:ss") {
      return moment(value).format(format);
    }
  },
  methods: {
    // 删除文章
    removeArticle(article_id) {
      this.$confirm("此操作将永久删除该文章, 是否继续?", "提示", {
        confirmButtonText: "删除",
        cancelButtonText: "留着",
        type: "warning"
      }).then(() => {
        this.axios
          .delete(`${this.settings.Host}/article_del/${article_id}/`)
          .then(response => {
            if (response.status == 204) {
              this.$emit("removeItem");
            }
          })
          .catch(error => {
            console.log(error);
          });
      });
    }
  }
};
</script>

<style lang="less" rel="stylesheet/less">
.article {
  background-color: #fff;
  padding: 20px 20px 10px;
  border-radius: 10px;
  margin-bottom: 20px;
  .header {
    display: flex;
    margin-bottom: 10px;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    .avatar {
      display: inline-block;
      height: 50px;
      width: 50px;
      border-radius: 50%;
      vertical-align: middle;
      overflow: hidden;
      box-shadow: 0 0 0 2px #fff, 0 0 0 3px #128ffd,
        0 8px 16px 0 rgba(0, 0, 0, 0.15);
      .img {
        height: inherit;
        width: inherit;
      }
    }
    .user-info {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      flex-grow: 1;
      padding-left: 10px;
      .name {
        font-weight: 700;
        color: #329dff;
        font-size: 18px;
      }
      .article-info {
        .pub-date {
          margin-right: 30px;
          font-size: 14px;
          color: #999;
        }
      }
    }
    .more-operate {
      display: inline-block;
      width: 20px;
      text-align: center;
      line-height: 50px;
      i {
        padding: 5px 10px;
        transition: all 0.3s;
        &:hover {
          background-color: #eee;
          border-radius: 5px;
        }
      }
    }
  }
  .article-header {
    .title {
      font-size: 2rem;
      color: #333;
      font-weight: 600;
      line-height: 40px;
      margin-bottom: 20px;
      a {
        color: #333;
        &:hover {
          color: #0c90fd;
        }
      }
    }
    .tags {
      display: flex;
      flex-wrap: nowrap;
      span {
        display: inline-block;
        padding: 5px 10px;
        margin-right: 10px;
        font-size: 14px;
        line-height: 14px;
        background-color: #a3d5ff;
        color: #0c90fd;
        cursor: pointer;
      }
    }
  }
  .body {
    max-height: 300px;
    padding: 10px 0;
    line-height: 30px;
    overflow: hidden;
    font-size: 1rem;
    font-weight: 400;
    color: #212529;
    text-align: left;
    .hljs-center {
      text-align: center;
    }
    .hljs-left {
      text-align: left;
    }
    .hljs-right {
      text-align: right;
    }
    article,
    aside,
    figcaption,
    figure,
    footer,
    header,
    hgroup,
    main,
    nav,
    section {
      display: block;
    }
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    .h1,
    .h2,
    .h3,
    .h4,
    .h5,
    .h6 {
      margin-bottom: 1rem;
      font-weight: 500;
      line-height: 1.2;
    }
    h1,
    .h1 {
      font-size: 32/16rem;
      border-bottom: 1px solid #eee;
      padding-bottom: 10px;
    }

    h2,
    .h2 {
      font-size: 28/16rem;
    }

    h3,
    .h3 {
      font-size: 24/16rem;
    }

    h4,
    .h4 {
      font-size: 20/16rem;
    }

    h5,
    .h5 {
      font-size: 1rem;
    }

    h6,
    .h6 {
      font-size: 0.75rem;
    }
    hr {
      margin-top: 1rem;
      margin-bottom: 1rem;
      border: 0;
      border-top: 1px solid rgba(0, 0, 0, 0.1);
    }
    code {
      font-size: 87.5%;
      font-family: "Source Code Pro", Consolas, Menlo, Monaco, "Courier New",
        monospace;
      color: #e83e8c;
      padding: 2px 4px;
      word-wrap: break-word;
      background-color: #f9f2f4;
      border-radius: 4px;
    }
    pre {
      display: block;
      margin-bottom: 16px;
      padding: 1rem;
      font-size: 87.5%;
      color: #212529;
      background: #f8f8f8;
      line-height: 1.45;
    }
    pre code {
      color: inherit;
      word-break: normal;
      background: none;
      font-size: 1rem;
      overflow-wrap: normal;
      white-space: inherit;
    }
    a > code {
      color: inherit;
    }
    kbd {
      padding: 0.2rem 0.4rem;
      font-size: 87.5%;
      color: #fff;
      background-color: #212529;
      border-radius: 0.2rem;
    }

    kbd kbd {
      padding: 0;
      font-size: 100%;
      font-weight: 700;
    }
    p {
      margin-bottom: 1rem;
      font-size: 1rem;
    }
    img {
      position: static !important;
      max-width: 100%;
      padding: 3px;
      margin-bottom: 1rem;
      border: 1px solid #ddd;
      vertical-align: middle;
      cursor: zoom-in;
    }
    table {
      width: 100%;
      margin-bottom: 1rem;
      border-collapse: collapse;
      th,
      td {
        border-bottom: 1px solid #ebeef5;
        border: 1px solid #e6e6e6;
        padding: 5px 8px;
        word-break: normal;
      }
      th {
        color: #333;
        font-weight: 600;
        background: #f3f3f3;
      }
      td {
        font-size: 14px;
        color: #606266;
      }
    }
    ol,
    ul,
    dl {
      margin-left: 3em;
      padding-left: 0;
      margin-bottom: 1rem;
    }

    ol ol,
    ul ul,
    ol ul,
    ul ol {
      margin-bottom: 0;
    }
    li {
      margin: 0.3rem 0;
      list-style: disc;
    }
    dt {
      font-weight: 700;
    }
    dd {
      margin-bottom: 0.5rem;
      margin-left: 0;
    }
    blockquote {
      margin-bottom: 1rem;
      padding: 10px 20px;
      border-left: 2px solid #329dff;
      background: #f6f6f6;
      color: #555;
      font-size: 1em;
      p {
        margin: 0;
      }
    }

    b,
    strong {
      font-weight: bolder;
    }

    small {
      font-size: 80%;
    }

    sub,
    sup {
      position: relative;
      font-size: 75%;
      line-height: 0;
      vertical-align: baseline;
    }

    sub {
      bottom: -0.25em;
    }

    sup {
      top: -0.5em;
    }

    a {
      color: #007bff;
      text-decoration: none;
      background-color: transparent;
      border-bottom: 1px solid #007bff66;
      padding-bottom: 1px;
    }

    a:hover {
      color: #0056b3;
      border-bottom: 1px solid #007bff;
    }

    a:not([href]) {
      color: inherit;
      text-decoration: none;
    }

    a:not([href]):hover {
      color: inherit;
      text-decoration: none;
    }
    em {
      font-style: italic;
    }
    address {
      background-color: #a6d1ff;
      border-radius: 2px;
    }
  }
  .update-time {
    font-size: 14px;
    color: #999;
  }
  .footer {
    border-top: 1px solid #e2e2e2;
    padding-top: 10px;
    span {
      display: inline-block;
      width: 100px;
      padding: 0 10px;
      color: #666;
    }
  }
}
.el-dropdown-menu {
  .el-dropdown-item {
    padding: 5px 20px;
    text-align: center;
    font-size: 14px;
    color: #666;
    cursor: pointer;
    a {
      color: #666;
    }
    &:hover {
      background-color: #ecf5ff;
      color: #66b1ff;
      a {
        background-color: #ecf5ff;
        color: #66b1ff;
      }
    }
  }
}
</style>