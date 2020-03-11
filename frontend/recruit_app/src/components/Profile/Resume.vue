<template>
  <div class="resume">
    <div class="container">
      <div class="header">
        <span class="avatar">
          <img class="img" :src="`${this.settings.Host}${resume.userinfo.avatar}`">
        </span>
        <div class="user-info">
          <span class="name"><a :href="`/user/${resume.user}/`" target="_blank">{{ resume.userinfo.nic_name }}</a></span>
          <p class="article-info">
            <span class="pub-date">发布于：{{ resume.pub_date }}</span>
          </p>
        </div>
      </div>
      <div class="body" v-html="resume.html_code"></div>
      <div class="footer">
        <p>更新于：{{ resume.update_date }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      resume: {}
    }
  },
  created () {
    let resume_id = this.$route.params.id;
    this.getResume(resume_id);
  },
  methods: {
    getResume (resume_id) {
      this.axios.get(`${this.settings.Host}/resume/${resume_id}/`)
      .then(response => {
        this.resume = response.data;
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style lang="less" rel="stylesheet/less">
.resume {
  background-color: #f6f6f6;
  .container {
    .header {
      display: flex;
      padding: 20px 50px;
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
        box-shadow: 0 0 0 2px #fff, 0 0 0 3px #128ffd, 0 8px 16px 0 rgba(0,0,0,.15);
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
          font-size: 18px;
          a {
            color: #329dff;
          }
        }
        .article-info {
          .pub-date {
            font-size: 14px;
            color: #999;
          }
        }
      }
    }
    .body {
      padding: 20px 50px;
      margin: 0 50px;
      font-size: 18px;
      line-height: 30px;
      font-size: 1rem;
      font-weight: 400;
      color: #212529;
      text-align: left;
      background: #fff;
      .hljs-center {
        text-align: center;
      }
      .hljs-left {
        text-align: left;
      }
      .hljs-right {
        text-align: right;
      }
      article, aside, figcaption, figure, footer, header, hgroup, main, nav, section {
        display: block;
      }
      h1, h2, h3, h4, h5, h6,
      .h1, .h2, .h3, .h4, .h5, .h6 {
        margin-bottom: 1rem;
        font-weight: 500;
        line-height: 1.2;
      }
      h1, .h1 {
        font-size: 32/16rem;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
      }

      h2, .h2 {
        font-size: 28/16rem;
      }

      h3, .h3 {
        font-size: 24/16rem;
      }

      h4, .h4 {
        font-size: 20/16rem;
      }

      h5, .h5 {
        font-size: 1rem;
      }

      h6, .h6 {
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
        font-family: "Source Code Pro",Consolas,Menlo,Monaco,"Courier New",monospace;
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
        th, td {
          border-bottom: 1px solid #ebeef5;
          border: 1px solid #E6E6E6;
          padding: 5px 8px;
          word-break: normal;
        }
        th {
          color: #333;
          font-weight: 600;
          background: #F3F3F3;
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
        margin: .3rem 0;
        list-style: disc;
      }
      dt {
        font-weight: 700;
      }
      dd {
        margin-bottom: .5rem;
        margin-left: 0;
      }
      blockquote {
        margin-bottom: 1rem;
        padding: 10px 20px;
        border-left: 2px solid #329dff;
        background: #F6F6F6;
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
        bottom: -.25em;
      }

      sup {
        top: -.5em;
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
    .footer {
      padding: 20px 50px;
      p {
        font-size: 14px;
        color: #999;
      }
    }
  }
}
</style>