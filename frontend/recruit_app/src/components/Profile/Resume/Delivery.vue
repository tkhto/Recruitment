<template>
  <div class="delivery">
      <div class="container">
            <header>投递记录</header>
            <el-card class="box-card">
                <div class="text item">
                    <table v-if="tableData">
                        <tr>
                            <th>投递时间</th>
                            <th>职位</th>
                            <th>简历状态</th>
                            <th>移除</th>
                        </tr>
                        <tr v-for="(item, i) in tableData" :key="i">
                            <td><h1>{{ item.create_time | dateStr }}</h1></td>
                            <td><el-link :href="`/position/${item.position__id}`" target="_blank" :underline="false">{{ item.position__positionName }}</el-link></td>
                            <td>
                                <el-tag v-if="item.status == false" size="small" type="info">未查看</el-tag>
                                <el-tag v-if="item.status == true" size="small" type="success">已查看</el-tag>
                            </td>
                            <td>
                                <el-button
                                v-if="item.status == true"
                                size="mini"
                                type="danger"
                                @click="handleDelete(item.pk)">删除</el-button>
                                <el-tag type="info" size="small" v-if="item.status == false">不能操作</el-tag>
                            </td>
                        </tr>
                    </table>
                    <div class="no-data" v-else>
                        <embed class="bg" src="../../../static/imgs/no_data.svg">
                        <h1 class="desc">没有记录</h1>
                    </div>
                </div>
            </el-card>
      </div>
  </div>
</template>

<script>
import moment from "moment";
export default {
    data () {
        return {
            user_id: '',
            tableData: []
        }
    },
    filters: {
        dateStr: function(value, format="YYYY-MM-DD HH:mm:ss") {
            return moment(value).format(format);
        },
    },
    created () {
        this.user_id = sessionStorage.user_id;
        this.get_delivery_record();
    },
    methods: {
        async get_delivery_record () {
            let response = await this.axios.get(`${this.settings.Host}/delivery/user/${this.user_id}/`)
            this.tableData = response.data.data;
        },
        handleDelete(pk) {
            this.axios.get(`${this.settings.Host}/delivery/delete/${pk}/?type=delivery`)
            .then(res => {
                if (res.data.status == 200) {
                    this.get_delivery_record()
                }
            }).catch(err => {
                console.log(err)
            })
        },
    }
}
</script>

<style lang="less" rel="stylesheet/less">
.delivery {
    min-height: 500px;
    .container {
        header {
            width: 840px;
            margin: 0 auto;
            padding: 20px 0;
            font-size: 32px;
            color: #333;
        }
        .box-card {
            width: 840px;
            margin: 0 auto 20px;
            .item {
                table {
                    width: 100%;
                    tr {
                        height: 50px;
                        line-height: 50px;
                        text-align: left;
                        border-bottom: 1px solid #e6e6e6;
                        td {
                            h1 {
                                color: #606266;
                                font-size: 14px;
                            }
                        }
                    }
                }
                .no-data {
                    position: relative;
                    text-align: center;
                    .bg {
                        width: 400px;
                    }
                    .desc {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        color: #333;
                    }
                }
            }
        }
    }
}
</style>