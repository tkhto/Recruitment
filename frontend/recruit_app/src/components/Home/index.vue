<template>
  <div class="home">
    <div class="search-panel">
      <div class="container">
        <div class="search-wrapper">
          <input type="text" placeholder="你想从事什么工作？"><button><i class="el-icon-right"></i></button>
        </div>
      </div>
    </div>
    <div class="hero">
      <div class="container">
        <el-row>
          <el-col :span="5">
            <ul class="menu-wrapper">
              <li class="menu-item" v-for="item in jobs" :key=item.id>
                <span>{{ item.name }}</span>
                <a href="javascript:;">{{ item['sub_category'][0]['name'] }}</a>
                <a href="javascript:;">{{ item['sub_category'][1]['name'] }}</a>
                <i class="el-icon-arrow-right"></i>
                <div class="sub-menu">
                  <dl v-for="sub_cate in item['sub_category']" :key=sub_cate.id>
                    <dt><span>{{ sub_cate.name }}</span></dt>
                    <dd><a href="javascript:;" v-for="cate in sub_cate['category']" :key=cate.id>{{ cate.name }}</a></dd>
                  </dl>
                </div>
              </li>
            </ul>
          </el-col>
          <el-col :span="19">
            <el-carousel :interval="5000" arrow="always" height="25rem">
              <el-carousel-item v-for="item in 4" :key="item">
                <h3>{{ item }}</h3>
              </el-carousel-item>
            </el-carousel> 
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="position">
      <div class="container">
        <h1>工作 <router-link tag="span" to="/positions">更多>>></router-link></h1>
        <el-row :gutter="20">
          <el-col :span="6" v-for="(item, index) in positions" :key="index">
            <router-link tag="div" :to="'position/'+item.id" class="grid-content">
              <p class="title">
                <span class="pos-name">{{ item.positionName }}</span>
                <span class="pos-salary">{{ item.salary }}</span>
              </p>
              <p class="pos-require">
                <span class="pos-year">{{ item.workYear }}</span> /
                <span class="pos-edu">{{ item.education }}</span>
              </p>
              <p class="pos-label">
                <span v-for="(label, id) in item.skillLabels" :key="id">{{ label }}</span>
              </p>
            </router-link>
          </el-col>
        </el-row>
        <h1>公司 <router-link tag="span" to="/companys">更多>>></router-link></h1>
        <el-row :gutter="20">
          <el-col :span="6" v-for="item in companys" :key="item.id">
            <router-link tag="div" :to="'company/'+item.companyId" class="grid-content">
              <div class="com-avatar"><img :src=item.companyLogo alt=""></div>
              <div class="com-info">
                <p class="com-name">{{ item.companyShortName }}</p>
                <p class="com-field"><span>{{ item.industryField }}</span> / <span>{{ item.financeStage }}</span></p>
                <p class="com-intro">{{ item.companyIntro }}</p>
              </div>
            </router-link>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data () {
    return {
      jobs: [],
      positions: [],
      companys: [],
      rec: [],
      searchCon: "",
    }
  },
  created () {
    this.getJobs()
    this.getPosition()
    this.getCompany()
  },
  methods: {
    async getJobs () {
      let response = await this.axios.get(`${this.settings.Host}/home/jobs/`)
      this.jobs = response.data
    },
    async getPosition () {
      let response = await this.axios.get(`${this.settings.Host}/home/position/?page=1&size=16`)
      this.positions = response.data.results
    },
    async getCompany () {
      let response = await this.axios.get(`${this.settings.Host}/home/company/?page=1&size=8`)
      this.companys = response.data.results
    }
  }
}
</script>

<style lang="less" rel="stylesheet/less" scoped>
.home {
  overflow: hidden;
  .search-panel {
    background-color: #f6f6f6;
    .container {
      .search-wrapper {
        display: flex;
        justify-content: space-between;
        flex-wrap: nowrap;
        height: 46/16rem;
        width: 696/16rem;
        margin: 50/16rem auto;
        border: 2/16rem solid #1c70f8;
        border-radius: 5/16rem;
        transition: all .3s;
        input {
          height: 30/16rem;
          padding: 8/16rem;
          flex-grow: 1;
          color: #5a5a5a;
          font-weight: 500;
          border-radius: 5/16rem 0 0 5/16rem;
        }
        button {
          height: 46/16rem;
          width: 50/16rem;
          font-size: 35/16rem;
          line-height: 46/16rem;
          border-radius: 0 5/16rem 5/16rem 0;
          i {
            color: #005bea;
          }
        }
        &:hover {
          transform: translate3d(0, -0.125rem, 0);
          box-shadow: -2px 4px 0px 0px #3a87ff;
        }
      }
    }
  }
  .hero {
    margin-top: 20/16rem;
    .container {
      .el-row {
        .el-col {
          height: 400/16rem;
          .menu-wrapper {
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            .menu-item {
              display: flex;
              justify-content: space-between;
              padding: 0 10/16rem;
              height: 50/16rem;
              line-height: 50/16rem;
              cursor: pointer;
              background-image: linear-gradient(to right, #fff 0%, #fff 100%);
              transition: all .3s;
              & > span {
                font-size: 16/16rem;
                font-weight: 500;
                color: #333;
              }
              a {
                font-size: 14/16rem;
                color: #555;
              }
              i {
                line-height: 50/16rem;
                color: #555;
                transition: all .3s;
              }
              &:hover {
                background-image: linear-gradient(to right, #00c6fb 0%, #005bea 100%);
                & > span {
                  color: #fff;
                }
                & > a {
                  color: #fff;
                }
                & > i {
                  transform: translateX(-5/16rem);
                  color: #fff;
                }
                .sub-menu {
                  display: block;
                }
              }
              .sub-menu {
                position: absolute;
                width: 700/16rem;
                height: 400/16rem;
                top: 0;
                left: 250/16rem;
                display: none;
                padding: 5/16rem;
                box-sizing: border-box;
                overflow: auto;
                z-index: 999;
                background-color: #fff;
                border: 1/16rem solid #005bea;
                 & > dl {
                  dt {
                    height: 35/16rem;
                    line-height: 35/16rem;
                    font-size: 16/16rem;
                    font-weight: 600;
                    color: #333;
                    & > span {
                      padding: 0 15/16rem;
                      line-height: 35/16rem;
                    }
                  }
                  dd {
                    line-height: 35/16rem;
                    & > a {
                      position: relative;
                      display: inline-block;
                      padding: 0 15/16rem;
                      font-size: 14/16rem;
                      line-height: 35/16rem;
                      color: #333;
                      &:hover {
                        color: #005bea;
                      }
                    }
                  }
                }
              }
            }
          }
          .el-carousel__item h3 {
            color: #475669;
            font-size: 18/16rem;
            opacity: 0.75;
            line-height: 400/16rem;
            margin: 0;
          }
          .el-carousel__item:nth-child(2n) {
            background-color: #99a9bf;
          }
          .el-carousel__item:nth-child(2n+1) {
            background-color: #d3dce6;
          }
          .login-panel {
            height: inherit;
            padding: 20/16rem;
            .el-avatar {
              display: flex;
              justify-content: space-around;
              margin: 0 auto;
              margin-bottom: 22/16rem;
            }
            .el-form {
              .el-button {
                width: 100%;
              }
            }
          }
        }
      }
    }
  }
  .position {
    margin-top: 20/16rem;
    background-color: #f9f9f9;
    .container {
      h1 {
        font-weight: 400;
        color: #1f2f3d;
        font-size: 28/16rem;
        padding-top: 20/16rem;
        span {
          font-size: 15/16rem;
          color: #dd4a38;
          cursor: pointer;
        }
      }
      .el-row {
        padding-bottom: 20/16rem;
        &:last-child {
          margin-bottom: 0;
        }
        .el-col {
          border-radius: 4/16rem;
          padding-top: 20/16rem;
          .grid-content {
            border-radius: 4/16rem;
            padding: 20/16rem;
            color: #757575;
            background-color: #fff;
            transition: all .3s;
            &:hover {
              box-shadow: 0 0 0.7rem 3/16rem rgba(0, 0, 0, 0.1);
              transform: translate3d(0, -0.125rem, 0);
            }
            .title {
              display: flex;
              justify-content: space-around;
              flex-wrap: nowrap;
              height: 30/16rem;
              line-height: 30/16rem;
              .pos-name {
                flex-grow: 1;
                font-weight: 400;
                color: #333;
                font-size: 20/16rem;
                text-overflow: ellipsis;
                overflow: hidden;
                white-space: nowrap;
              }
              .pos-salary {
                padding-left: 10/16rem;
                color: #dd4a38;
                font-size: 20/16rem;
                font-weight: 800;
                min-width: fit-content;
              }
            }
            .pos-require {
              height: 30/16rem;
              line-height: 30/16rem;
              font-size: 15/16rem;
            }
            .pos-label {
              text-overflow: ellipsis;
              overflow: hidden;
              white-space: nowrap;
              span {
                height: 30/16rem;
                line-height: 30/16rem;
                padding: 3/16rem 10/16rem;
                background-color: #f1f1f1;
                font-size: 12/16rem;
                border-radius: 15/16rem;
              }
              span:not(last-child) {
                margin-right: 5/16rem;
              }
            }
            .com-avatar {
              height: 80/16rem;
              text-align: center;
              img {
                width: 80/16rem;
                height: 80/16rem;
              }
            }
            .com-info {
              padding-top: 10/16rem;
              text-align: center;
              color: #646464;
              p {
                height: 30/16rem;
                line-height: 30/16rem;
                font-size: 15/16rem;
                text-overflow: ellipsis;
                overflow: hidden;
                white-space: nowrap;
              }
            }
          }
          .row-bg {
            padding: 10/16rem 10/16rem;
            background-color: #f9fafc;
          }
        }
      }
    }
  }
}
</style>
