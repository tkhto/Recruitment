<template>
  <div class="article">
    <div class="container">
      <div class="article-content">
        <div class="header">
          <span class="avatar">
            <img class="img" :src="`${this.settings.Host}/`+article.userinfo.avatar" />
          </span>
          <div class="user-info">
            <span class="name">{{ article.userinfo.nic_name }}</span>
            <p class="article-info">
              <span class="pub-date">发布于：{{ article.update_date | dateStr }}</span>
              <span class="pub-date">阅读量：{{ article.read_num }}</span>
            </p>
          </div>
          <el-dropdown class="more-operate" trigger="hover">
            <span class="el-dropdown-link">
              <i class="fa fa-ellipsis-v"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <li class="el-dropdown-item">
                <a :href="`/editarticle/${article.id}`" target="_blank">
                  <i class="el-icon-edit-outline"></i> 修改
                </a>
              </li>
              <li class="el-dropdown-item" @click="removeArticle(article.id)">
                <i class="el-icon-delete"></i> 删除
              </li>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <div class="article-header">
          <header class="title">{{ article.title }}</header>
          <p class="tags">
            <span>AI</span>
            <span>NLP</span>
            <span>Web</span>
            <span>API</span>
          </p>
        </div>
        <div class="body" v-html="article.html_code"></div>
        <div class="update-time">
          <span>更新于：{{ article.pub_date | dateStr }}</span>
        </div>
        <div class="footer">
          <span>
            <i class="el-icon-s-management"></i> 收藏 0
          </span>
          <span>
            <i class="el-icon-star-on"></i> 赞 0
          </span>
        </div>
      </div>
      <div class="comment">
        <header><i class="el-icon-chat-line-square"></i> 评论</header>
        <div class="comment-input">
            <el-input placeholder="请输入评论内容" v-model="commentValue" class="input-with-select">
                <el-button slot="append" icon="el-icon-s-promotion" @click="submitComment(parent=0, reply=0, type='root')">提交</el-button>
            </el-input>
        </div>
        <div class="comment-item" v-for="(comment, i) in comments_list" :key="i">
            <el-avatar :size="size" :src="`http://api.offend.com:8000/${comment.user.avatar}`"></el-avatar>
            <div class="comment-content">
                <div class="detail">
                    <p class="text"><a href="" class="from-name">{{ comment.user.nic_name }}</a>&nbsp;:&nbsp;{{ comment.content }}</p>
                    <div class="status">
                      <span>{{ comment.create_time | endOf }}</span>
                      <span @click="showCommentInput(comment.cid)">回复</span>
                    </div>
                    <el-input placeholder="请输入评论内容" v-if="CommentId == comment.cid" v-model="subCommentValue" class="input-with-select">
                        <el-button slot="append" icon="el-icon-s-promotion" @click="submitComment(parent=comment.cid, reply=comment.cid)">提交</el-button>
                    </el-input>
                </div>
                <div class="sub" v-show="comment.sub_comment">
                    <div class="detail" v-for="(sub, i) in comment.sub_comment" :key="i">
                        <p class="text">
                          <a href="" class="from-name">{{ sub.user.nic_name }} <i v-show="article.userinfo.id == sub.user.uid">作者</i></a> @ 
                          <a href="" class="from-name">{{ sub.reply.nic_name }} <i v-show="article.userinfo.id == sub.reply.uid">作者</i></a>&nbsp;:&nbsp;{{ sub.content }}
                        </p>
                        <div class="status">
                          <span>{{ sub.create_time | endOf }}</span>
                          <span @click="showSubCommentInput(sub.cid)">回复</span>
                        </div>
                        <el-input placeholder="请输入评论内容" @blur="hideSubCommentInput()" v-if="subCommentId == sub.cid" v-model="subCommentValue" class="input-with-select subCommentInput">
                            <el-button slot="append" icon="el-icon-s-promotion" @click="submitComment(parent=comment.cid, reply=sub.cid)">提交</el-button>
                        </el-input>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  data() {
    return {
      article: {},
      article_id: "",
      commentValue: '',
      subCommentValue: '',
      size: 'medium',
      comments_list: [],
      CommentId: 0,
      subCommentId: 0
    };
  },
  created() {
    this.article_id = this.$route.params.id;
    this.getArticle(this.article_id);
    this.getComment();
  },
  filters: {
    dateStr: function(value, format="YYYY-MM-DD HH:mm:ss") {
      return moment(value).format(format);
    },
    endOf: function(value, format = "YYYYMMDD") {
      return moment(value, "YYYYMMDD").fromNow();
    }
  },
  methods: {
    // 获取文章信息
    getArticle(article_id) {
      console.log(article_id);
      this.axios
        .get(`${this.settings.Host}/article/${article_id}/`)
        .then(response => {
          this.article = response.data.result;
        });
    },
    // 获取评论
    getComment () {
      this.axios.get(`${this.settings.Host}/articlecomment/${this.article_id}`)
      .then(response => {
        this.comments_list = response.data
      }).catch(error => {
        console.log(error)
      })
    },
    // 提交评论
    submitComment (parent, reply, type='') {
      this.axios.post(`${this.settings.Host}/articlecomment/${this.article_id}`, {
        user: sessionStorage.user_id,
        parent: parent,
        reply: reply,
        article: this.article_id,
        content: type == "root" ? this.commentValue : this.subCommentValue
      }).then(response => {
        this.commentValue = '';
        this.subCommentValue = '';
        this.CommentId = 0;
        this.subCommentId = 0;
        this.getComment();
      }).catch(error => {
        console.log(error)
      })
    },
    showCommentInput(comment_id) {
      this.CommentId = comment_id;
      this.subCommentId = 0;
    },
    showSubCommentInput(subComment_id) {
      this.subCommentId = subComment_id;
      this.CommentId = 0;
    },
    hideSubCommentInput() {
      if (this.subCommentValue == '') {
        this.subCommentId = 0;
      }
    }
  }
};
</script>

<style lang="less" rel="stylesheet/less">
.article {
  background-color: #f6f6f6;
  padding-top: 20px;
  .container {
    .article-content {
      width: 800px;
      border-radius: 10px;
      margin: 0 auto 20px;
      padding: 20px;
      background-color: #fff;
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
        padding: 10px 0;
        line-height: 30px;
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
          overflow: auto;
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
          margin-bottom: 10px;
        font-size: 14px;
        color: #999;
      }
      .footer {
        display: flex;
        flex-wrap: nowrap;
        justify-content: center;
        text-align: center;
        cursor: pointer;
        span {
            display: inline-block;
            width: 100px;
            padding: 0 10px;
            color: #0076e2;
            height: 40px;
            line-height: 40px;
            border-radius: 5px;
            border: 1px solid #0076e2;
            transition: all .3s;
            &:hover {
                background-color: #0076e2;
                color: #fff;
            }
        }
        span:not(:last-child) {
            margin-right: 10px;
        }
      }
    }
    .comment {
        width: 800px;
        margin: 0 auto 20px;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        header {
            margin-bottom: 10px;
            font-size: 20px;
            color: #333;
            font-weight: 300;
            i {
              color: #333;
            }
        }
        .comment-input {
            margin-bottom: 20px;
            .el-input-group__append {
                background-color: #007bff;
                color: #fff;
                border: none;
            }
        }
        .comment-item {
            display: flex;
            margin-bottom: 10px;
            flex-wrap: nowrap;
            .el-avatar {
                margin-right: 10px;
            }
            .comment-content {
                flex-grow: 1;
                .detail {
                  line-height: 36px;
                  .text {
                    flex-grow: 1;
                    color: #333;
                    .from-name {
                        font-size: 16px;
                        font-weight: 500;
                        color: #007aff;
                    }
                  }
                  .status {
                    height: 20px;
                    margin-bottom: 10px;
                    line-height: 20px;
                    span {
                      font-size: 14px;
                      color: #979fa7;
                    }
                  }
                  .el-input {
                    margin-bottom: 10px;
                  }
                  .el-input-group__append {
                      background-color: #007bff;
                      color: #fff;
                      border: none;
                  }
                }
                .sub {
                  padding: 10px;
                  background-color: #f6f6f6;
                  border-radius: 5px;
                  .detail {
                    .text {
                      flex-grow: 1;
                      color: #333;
                      .from-name {
                        font-size: 16px;
                          font-weight: 500;
                          color: #007aff;
                        i {
                          background-color: #bdd5ff;
                          color: #007aff;
                          font-size: 14px;
                          line-height: 16px;
                          padding: 2px;
                          border-radius: 5px;
                        }
                      }
                    }
                    .status {
                      height: 20px;
                      margin-bottom: 10px;
                      line-height: 20px;
                      span {
                        font-size: 14px;
                        color: #979fa7;
                      }
                    }
                    .el-input {
                      margin-bottom: 10px;
                    }
                    .el-input-group__append {
                        margin-bottom: 10px;
                        background-color: #007bff;
                        color: #fff;
                        border: none;
                    }
                  }
                  .detail:not(:last-child) {
                    border-bottom: 1px solid #ddd;
                  }
                }
            }
        }
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
    &:hover, &:hover a {
      background-color: #ecf5ff;
      color: #66b1ff;
    }
  }
}
</style>