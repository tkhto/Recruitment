<template>
  <div class="posdetail">
    <div class="pos-header">
      <div class="container">
        <el-row>
          <el-col :span="18">
            <div class="grid-content">
              <div class="mid-wrapper">
                <p class="pos-name">{{ position.positionName }}</p>
                <p class="pos-require">
                  <span class="pos-salary"><i class="el-icon-money"></i> {{ position.salary }}</span>
                  <span><i class="el-icon-location-information"></i> {{ position.city }}</span>
                  <span><i class="el-icon-time"></i> 经验{{ position.workYear }}</span>
                  <span><i class="el-icon-medal"></i> {{ position.education }}</span>
                  <span><i class="el-icon-date"></i> {{ position.jobNature }}</span>
                </p>
              </div>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content">
              <div class="btn-wrapper">
                <a href="javascript:;"><i class="el-icon-position"></i> 投递简历</a>
                <a href="javascript:;"><i class="el-icon-star-off"></i> 收藏</a>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="pos-content">
      <div class="container">
        <el-row>
          <el-col :span="16">
            <div class="grid-content">
              <div class="pos-intro">
                <h1>职位诱惑：</h1>
                <p>{{ position.positionAdvantage }}</p>
                <h1>职位描述：</h1>
                <p>{{ position.positionIntro }}</p>
                <h1>工作地址</h1>
                <p>{{ position.city }} - {{ position.district }} - {{ position.subwayLine +""+ position.stationName }}</p>
              </div>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content">
              <div class="com-intro">
                <div class="com-avatar">
                  <img :src=position.company.companyLogo alt="">
                </div>
                <p class="com-name">{{ position.company.companyShortName }}</p>
                <p><i class="el-icon-aim"></i> {{ position.company.industryField }}</p>
                <p><i class="el-icon-finished"></i> {{ position.company.financeStage }}</p>
                <p><i class="el-icon-user"></i> {{ position.company.companySize }}</p>
                <p><i class="el-icon-link"></i> <a :href=position.company.companySite>{{ position.company.companySite }}</a></p>
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
  name: 'posdetail',
  data () {
    return {
      id: this.$route.params.id,
      position: []
    }
  },
  created () {
    this.getPosition()
  },
  methods: {
    async getPosition () {
      let response = await this.axios.get(`${this.settings.Host}/home/position/${this.id}/`)
      this.position = response.data
    }
  }
}
</script>

<style lang="less" rel="stylesheet/less">
.posdetail {
  .pos-header {
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
            .mid-wrapper {
              display: flex;
              padding: 0 60/16rem;
              height: inherit;
              justify-content: flex-end;
              flex-direction: column;
              .pos-name {
                height: 30/16rem;
                margin-bottom: 10/16rem;
                line-height: 30/16rem;
                font-size: 25/16rem;
                color: #444;
                font-weight: 200;
              }
              .pos-require {
                display: flex;
                justify-content: space-between;
                height: 30/16rem;
                line-height: 30/16rem;
                span {
                  font-size: 16/16rem;
                  color: #757575;
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
  .pos-content {
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
            .pos-intro {
              padding: 20/16rem 60/16rem;
              border-right: 1/16rem dashed #ddd;
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
            }
            .com-intro {
              padding: 20/16rem 60/16rem;
              .com-avatar {
                text-align: center;
                margin-bottom: 10/16rem;
                img {
                  width: 100/16rem;
                  height: inherit;
                  padding: 4/16rem;
                  background-color: #afafaf;
                  vertical-align: middle;
                }
              }
              p {
                height: 30/16rem;
                line-height: 30/16rem;
                margin-bottom: 10/16rem;
                color: #757575;
                a {
                  color: #757575;
                  &:hover {
                    color: #2b84f1;
                  }
                }
              }
              .com-name {
                text-align: center;
                font-size: 20/16rem;
                font-weight: 200;
                color: #333;
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
