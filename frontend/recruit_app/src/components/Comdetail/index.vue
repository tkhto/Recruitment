<template>
  <div class="comdetail">
    <div class="com-header">
      <div class="container">
        <el-row>
          <el-col :span="5">
            <div class="grid-content">
              <div class="com-avatar">
                <img v-if="company.companyLogo" :src="company.companyLogo">
                <img v-else src="https://www.lgstatic.com/thumbnail_300x300/i/image2/M01/3E/2E/CgotOVzxFqCAedwfAAAtOxHRS_0737.png" alt="">
              </div>
            </div>
          </el-col>
          <el-col :span="19">
            <div class="grid-content">
              <div class="mid-wrapper">
                <p class="com-name">{{ company.companyShortName }} <a :href=company.companySite>
                  <i class="el-icon-link"></i></a> <el-tooltip v-if="company.legalize" class="item" effect="dark" content="已认证" placement="right">
                  <i class="el-icon-success"></i></el-tooltip></p>
                <p class="com-intro">{{ company.signature }}</p>
                <p class="com-info">
                  <span><i class="el-icon-aim"></i> {{ company.industryField }}</span>
                  <span><i class="el-icon-finished"></i>  {{ company.financeStage }}</span>
                  <span><i class="el-icon-user"></i> {{ company.company_size }}</span>
                  <span><i class="el-icon-location-outline"></i> 上海</span>
                </p>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="com-content">
      <div class="container">
        <el-row>
          <el-col :span="16">
            <div class="grid-content">
              <div class="com-desc">
                <h1>公司介绍</h1>
                <p v-html="company.companyIntro"></p>
                <h1>公司位置</h1>
                <div id="container"></div>
              </div>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content">
              <div class="other-info">
                <h1>创始人信息</h1>
                <div class="creator-info">
                  <div class="img" v-if="company.createPersonAvatar" :style='{backgroundImage:url(company.createPersonAvatar)}'></div>
                  <div class="img" v-else style='background-image:url("https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png")'></div>
                  <div class="info-wrapper">
                    <p class="com-name">{{ company.createPerson }}</p>
                    <p>{{ company.createPersonIntro }}</p>
                  </div>
                </div>
                <h1>公司标签</h1>
                <div class="com-labels">
                  <span v-if="company.companyLabelList != ''" v-for="(item, i) in company.companyLabelList" :key="i">{{ item }}</span>
                  <p v-else>还没有添加标签</p>
                </div>
                <h1>工商信息</h1>
                <div class="bussiness-info">
                  <h2><i class="el-icon-coordinate"></i> 工商信息</h2>
                  <p>{{ company.companyFullName }}</p>
                  <h2><i class="el-icon-date"></i> 成立时间</h2>
                  <p>{{ company.createTime }}</p>
                  <h2><i class="el-icon-money"></i> 注册资本</h2>
                  <p>{{ company.capital }}万人民币</p>
                  <h2><i class="el-icon-user"></i> 法人代表</h2>
                  <p>{{ company.legalRepresentative }}</p>
                </div>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>



<script>
export default {
  name: 'comdetail',
  data () {
    return {
      id: this.$route.params.id,
      company: []
    }
  },
  mounted () {
    this.getCompany()
  },
  created () {
  },
  methods: {
    async getCompany () {
      let response = await this.axios.get(`${this.settings.Host}/home/company/${this.id}/`)
      this.company = response.data
      let map = new AMap.Map('container', {
        zoom: 20, // 放大级别
        center: [this.company.longitude, this.company.latitude],//中心点坐标
        viewMode: '3D' //使用3D视图
      });

      function initPage(SimpleMarker) {
        //内置的样式
        let iconStyles = SimpleMarker.getBuiltInIconStyles('fresh');
        let iconIdx = 3;
        let marker = new SimpleMarker({
            iconTheme: 'fresh',
            //使用内置的iconStyle
            iconStyle: iconStyles[iconIdx],
            //显示定位点
            showPositionPoint:true,
            map: map,
            position: map.getCenter()
        });
      }
      //加载SimpleMarker
      AMapUI.loadUI(['overlay/SimpleMarker'], function(SimpleMarker) {
          initPage(SimpleMarker);
      });
    }
  }
}
</script>

<style lang="less" rel="stylesheet/less">
.comdetail {
  .com-header {
    background-color: #f9f9f9;
    .container {
      .el-row {
        margin-bottom: 20/16rem;
        padding: 20/16rem 0;
        &:last-child {
          margin-bottom: 0;
        }
        .el-col {
          border-radius: 4/16rem;
          .grid-content {
            border-radius: 4/16rem;
            min-height: 36/16rem;
            height: 140/16rem;
            .row-bg {
              padding: 10/16rem 0;
              background-color: #f9fafc;
            }
            .com-avatar {
              height: inherit;
              text-align: center;
              img {
                height: inherit;
                vertical-align: middle;
              }
            }
            .mid-wrapper {
              display: flex;
              height: inherit;
              justify-content: flex-end;
              flex-direction: column;
              .com-name {
                height: 30/16rem;
                margin-bottom: 10/16rem;
                line-height: 30/16rem;
                font-size: 25/16rem;
                color: #444;
                font-weight: 200;
                a {
                  i {
                    color: #444;
                  }
                }
                i {
                  color: #47adff;
                }
              }
              .com-intro {
                height: 30/16rem;
                margin-bottom: 10/16rem;
                line-height: 30/16rem;
                font-size: 20/16rem;
                color: #444;
                font-weight: 200;
              }
              .com-info {
                height: 30/16rem;
                line-height: 30/16rem;
                span {
                  font-size: 16/16rem;
                  color: #757575;
                  margin-right: 20/16rem;
                  i {
                    color: #757575;
                  }
                }
                .pos-salary {
                  color: #dd4a38;
                  font-size: 20/16rem;
                  font-weight: 600;
                }
              }
            }
            .btn-wrapper {
              display: flex;
              height: inherit;
              padding: 0 60/16rem;
              justify-content: space-around;
              flex-direction: column;
              a {
                display: block;
                height: 40/16rem;
                line-height: 40/16rem;
                text-align: center;
                color: #fff;
                font-size: 16/16rem;
                background-color: #333;
                border-radius: 20/16rem;
                transition: all .3s;
                &:hover {
                  box-shadow: 0 0.9375rem 1.875rem rgba(0, 0, 0, 0.1);
                  transform: translate3d(0, -0.125rem, 0);
                  /*color: #333;*/
                  background-color: #000;
                }
              }
            }
          }
        }
      }
    }
  }
  .com-content {
    border-bottom: 1/16rem dashed #ddd;
    .container {
      .el-row {
        margin-bottom: 20/16rem;
        &:last-child {
          margin-bottom: 0;
        }
        .el-col {
          border-radius: 4/16rem;
          .grid-content {
            border-radius: 4/16rem;
            min-height: 36/16rem;
            .com-desc {
              padding: 20/16rem 60/16rem;
              h1 {
                height: 30/16rem;
                line-height: 30/16rem;
                font-size: 20/16rem;
                font-weight: 500;
                color: #333;
                margin-bottom: 10/16rem;
              }
              p {
                margin-bottom: 10/16rem;
                font-size: 16/16rem;
                color: #444;
                line-height: 30/16rem;
              }
              #container {
                width: 100%;
                height: 400/16rem;
              }
            }
            .other-info {
              padding: 20/16rem 40/16rem;
              border-left: 1/16rem dashed #ddd;
              div {
                margin-bottom: 20/16rem;
              }
              h1 {
                height: 30/16rem;
                line-height: 30/16rem;
                font-size: 20/16rem;
                margin-bottom: 20/16rem;
                padding-left: 10/16rem;
                border-left: 5/16rem solid #47adff;
                font-weight: 200;
                color: #333;
              }
              .creator-info {
                overflow: hidden;
                height: 100/16rem;
                .img {
                  width: 100/16rem;
                  height: 100/16rem;
                  margin-right: 20/16rem;
                  float: left;
                  border-radius: 50%;
                  vertical-align: middle;
                  background-size: cover;
                }
                .info-wrapper {
                  height: 100/16rem;
                  overflow: hidden;
                  p {
                    height: 30/16rem;
                    margin-bottom: 10/16rem;
                    line-height: 30/16rem;
                    color: #757575;
                    font-size: 14/16rem;
                  }
                  .com-name {
                    font-size: 20/16rem;
                    font-weight: 200;
                    color: #333;
                  }
                }
              }
              .com-labels {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                span {
                  display: inline-block;
                  height: 30/16rem;
                  padding: 0/16rem 13/16rem;
                  margin-bottom: 10/16rem;
                  border: 1/16rem solid #bfbfbf;
                  background-color: #ddd;
                  line-height: 30/16rem;
                  color: #313131;
                  font-size: 13/16rem;
                  border-radius: 16/16rem;
                }
                p {
                  height: 30/16rem;
                  margin-bottom: 10/16rem;
                  line-height: 30/16rem;
                  color: #808080;
                  font-size: 14/16rem;
                  text-indent: 20/16rem;
                }
              }
              .bussiness-info {
                h2 {
                  height: 30/16rem;
                  line-height: 30/16rem;
                  color: #3c3c3c;
                  font-size: 16/16rem;
                }
                p {
                  height: 30/16rem;
                  margin-bottom: 10/16rem;
                  line-height: 30/16rem;
                  color: #808080;
                  font-size: 14/16rem;
                  text-indent: 20/16rem;
                }
              }
            }
          }
        }
        .row-bg {
          padding: 10/16rem 0;
          background-color: #f9fafc;
        }
      }
    }
  }
}
</style>
