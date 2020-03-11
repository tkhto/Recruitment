<template>
    <div class="footer">
      <div class="footer-service">
        <div class="container">
          <div class="footer-left">
            <div class="img">
              <img src="https://www.lgstatic.com/thumbnail_160x160/i/image2/M01/3E/2E/CgotOVzxFqCAedwfAAAtOxHRS_0737.png" alt="">
            </div>
            <div class="img-desc"><span>企业公众号</span></div>
          </div>
          <div class="footer-wrapper">
            <dl>
              <dt>企业服务</dt>
              <dd>招聘宝典</dd>
              <dd>公司搜索</dd>
            </dl>
            <dl>
              <dt>用户帮助</dt>
              <dd>帮助中心</dd>
              <dd>隐私政策</dd>
              <dd>用户服务协议</dd>
              <dd>在线提问</dd>
            </dl>
            <dl>
              <dt>联系方式</dt>
              <dd>服务热线</dd>
              <dd>企业邮箱</dd>
              <dd>联系我们</dd>
              <dd>关于团队</dd>
            </dl>
          </div>
        </div>
      </div>
      <div class="footer-copyright">
        <div class="container">
          <p class="copyright">©2020 offend 京ICP备14023245号-2 <i></i> 京公网安备 110134345024043号</p>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "footer"
    }
</script>

<style lang="less" rel="stylesheet/less">
.footer {
  .footer-service {
    padding: 20/16rem 0;
    .container {
      .footer-left {
        float: left;
        width: 300/16rem;
        .img {
          text-align: center;
          img {
            width: 100/16rem;
            height: 100/16rem
          }
        }
        .img-desc {
          text-align: center;
          margin-top: 20/16rem;
          span {
            display: inline-block;
            height: 30/16rem;
            padding: 2/16rem 10/16rem;
            line-height: 30/16rem;
            font-size: 16/16rem;
            border: 1/16rem dashed #909090;
            color: #757575;
            background-color: #f5f5f5;
          }
        }
      }
      .footer-wrapper {
        display: flex;
        justify-content: space-around;
        flex-wrap: nowrap;
        dl {
          float: left;
          width: 200/16rem;
          dt {
            font-size: 20/16rem;
            margin-bottom: 20/16rem;
            height: 25/16rem;
            line-height: 25/16rem;
            color: #333;
            font-weight: 200;
          }
          dd {
            height: 25/16rem;
            line-height: 25/16rem;
            font-size: 16/16rem;
            font-weight: 200;
            color: #444;
            margin: 5/16rem 0;
          }
        }
      }
    }
  }
  .footer-copyright {
    background-color: #f9f9f9;
    color: #525252;
    height: 100/16rem;
    line-height: 100/16rem;
    text-align: center;
    .container {
      .copyright {
        i {
          display: inline-block;
          width: 16/16rem;
          vertical-align: middle;
          height: 17/16rem;
          background: url(https://www.lgstatic.com/lg-www-fed/common/widgets/footer_c/modules/img/sprite_9dd5c92.png) -10/16rem -44/16rem no-repeat;
          background-size: 128/16rem 128/16rem;
        }
      }
    }
  }
}
</style>
