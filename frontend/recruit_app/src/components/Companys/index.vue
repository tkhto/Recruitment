<template>
  <div class="companys">
    <div class="search-panel">
      <div class="container">
        <el-row>
          <el-col :span="16" :offset="4">
            <el-input placeholder="搜索职位" v-model="searchCon">
              <template slot="append">
                <el-button>
                  <i class="el-icon-search"></i> 搜索
                </el-button>
              </template>
            </el-input>
          </el-col>
        </el-row>
      </div>
    </div>
    <div class="filter-panel">
      <div class="container">
        <div class="filter-list">
            <div class="filter-wrapper">
                <span class="label">经营领域 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in industryFieldOption" :key="id" @click="filterIndustryField(item)">{{ item }}</span>
                </div>
            </div>
            <div class="filter-wrapper">
                <span class="label">公司规模 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in companySizeOption" :key="id" @click="filterCompanySize(id-1)">{{ item }}</span>
                </div>
            </div>
            <div class="filter-wrapper">
                <span class="label">融资情况 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in financeStageOption" :key="id" @click="filterFinanceStage(item)">{{ item }}</span>
                </div>
            </div>
            <div class="filter-wrapper">
                <span class="label">是否认证 <i class="el-icon-caret-right"></i></span>
                <div class="item">
                    <span class="filter-item" v-for="(item, id) in legalizeOption" :key="id" @click="filterLegalize(id-1)">{{ item }}</span>
                </div>
            </div>
        </div>
      </div>
    </div>
    <div class="filter-require">
      <div class="container">
        <div class="require">
          <span>经营领域: <i v-if="filters.industryField">{{ filters.industryField }}</i><i v-else>不限</i></span>
          <span>公司规模: <i v-if="filters.companySize || filters.companySize === 0">{{ companySizeLabel[filters.companySize] }}</i><i v-else>不限</i></span>
          <span>融资情况: <i v-if="filters.financeStage">{{ filters.financeStage }}</i><i v-else>不限</i></span>
          <span>是否认证: <i v-if="filters.legalize || filters.legalize === 0">{{ legalizeLabel[filters.legalize] }}</i><i v-else>不限</i></span>
        </div>
      </div>
    </div>
    <div class="com-list">
      <div class="container">
        <el-row :gutter="20">
          <el-col :span="6" v-for="item in companys.results" :key="item.id">
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
        <el-pagination background 
        @current-change="handleCurrentChange"
        layout="prev, pager, next" 
        :page-size="8"
        :total="companys.count">
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'company',
  data() {
    return {
      companys: [],
      filters: {
          page: 1,
          companySize: '',
          industryField: '',
          financeStage: '',
          legalize: ''
      },
      companySizeOption: [],
      industryFieldOption: [],
      financeStageOption: [],
      legalizeOption: [],
      companySizeLabel: ["15-50",  "50-150",  "150-500", "500-2000", "2000以上"],
      legalizeLabel: ['未认证', '已认证']
    };
  },
  created() {
    this.getCompany();
    this.ComFilterRequire();
  },
  watch: {
    "filters.page" () {
      this.getCompany();
    },
    "filters.companySize" () {
      this.getCompany();
    },
    "filters.industryField" () {
      this.getCompany();
    },
    "filters.financeStage" () {
      this.getCompany();
    },
    "filters.legalize" () {
      this.getCompany();
    }
  },
  methods: {
    // 获取公司列表
    async getCompany() {
      let response = await this.axios.get(`${this.settings.Host}/home/company/`, {
          params: this.filters
      });
      this.companys = response.data;
    },
    // 当前页码发生改变时
    handleCurrentChange (page) {
      this.filters.page = page;
    },
    // 获取查询条件
    async ComFilterRequire() {
      let response = await this.axios.get(`${this.settings.Host}/home/ComFilterRequire/`)
        this.companySizeOption = response.data.all_companySize
        this.industryFieldOption = response.data.all_industryField
        this.financeStageOption = response.data.all_financeStage
        this.legalizeOption = response.data.all_legalize
        this.companySizeOption.unshift('不限')
        this.industryFieldOption.unshift('不限')
        this.financeStageOption.unshift('不限')
        this.legalizeOption.unshift('不限')
    },
    filterIndustryField (item) {
      if (item == '不限') {
            this.filters.industryField = '';
        } else {
            this.filters.industryField = item;
        }
    },
    filterCompanySize (item) {
      if (item == '-1') {
            this.filters.companySize = '';
        } else {
            this.filters.companySize = item;
        }
    },
    filterFinanceStage (item) {
      if (item == '不限') {
            this.filters.financeStage = '';
        } else {
            this.filters.financeStage = item;
        }
    },
    filterLegalize (item) {
      if (item == '-1') {
            this.filters.legalize = '';
        } else {
            this.filters.legalize = item;
        }
    }
  }
}
</script>

<style rel="stylesheet/less" lang="less" scoped>
.companys {
  overflow: hidden;
  .search-panel {
    background-color: #f9f9f9;
    .container {
      .el-row {
        width: 1200/16rem;
        margin: 45/16rem 0/16rem;
        .el-col {
          border-radius: 4/16rem;
        }
      }
    }
  }
  .filter-panel {
    .container {
      .filter-list {
        padding: 20/16rem 30/16rem;
        margin: 30/16rem 0;
        color: #333;
        border-radius: 8/16rem;
        background-color: #f9f9f9;
        box-shadow: 0 0 0 0 #333;
        .filter-wrapper {
            display: flex;
            justify-content: space-around;
            flex-wrap: nowrap;
            height: 36/16rem;
            .label {
                height: 30/16rem;
                line-height: 30/16rem;
                padding: 3/16rem 5/16rem;
                white-space: nowrap;
                i {
                    transition: all .5s;
                }
            }
            .item {
                display: flex;
                padding: 3/16rem;
                justify-content: flex-start;
                flex-wrap: wrap;
                flex-grow: 1;
                height: 30/16rem;
                line-height: 30/16rem;
                overflow: hidden;
                font-size: 14/16rem;
                .filter-item {
                    padding: 0 5/16rem;
                    line-height: 20/16rem;
                    height: 20/16rem;
                    margin: 5/16rem 0/16rem;
                    margin-right: 7/16rem;
                    transition: all 0.3s;
                    cursor: pointer;
                    &:hover {
                        color: #fff;
                        background-color: #005bea;
                    }
                }
            }
            &:hover {
                .item {
                    height: fit-content;
                    padding: 2/16rem;
                    max-height: 132/16rem;
                    z-index: 999;
                    background-color: rgb(255, 255, 255);
                    overflow: scroll;
                    border: 1/16rem solid #005bea;
                }
                .label {
                    background-color: #005bea;
                    color: #fff;
                    i {
                      transform: rotateZ(90deg)
                    }
                }
            }
        }
      }
    }
  }
  .filter-require {
    .container {
      .require {
        padding: 15/16rem 30/16rem;
        background-color: #f9f9f9;
        border-radius: 8/16rem;
        span {
          margin-right: 20/16rem;
          color: #333;
          i {
            border: 1/16rem dashed #005bea;
            padding: 0/16rem 3/16rem;
            color: #005bea;
            font-size: 14/16rem;
          }
        }
      }
    }
  }
  .com-list {
    border-bottom: 1/16rem dashed #ddd;
    .container {
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
      .el-pagination {
          padding: 20/16rem;
          margin-bottom: 20/16rem;
          text-align: center;
        }
    }
  }
}
</style>