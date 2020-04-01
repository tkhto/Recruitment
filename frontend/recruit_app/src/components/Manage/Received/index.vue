<template>
  <div class="received">
      <div class="container">
            <header>已收简历</header>
            <el-card class="box-card">
                <div class="text item">
                    <table v-if="tableData == []">
                        <tr>
                            <th>投递时间</th>
                            <th>投递用户</th>
                            <th>职位</th>
                            <th>用户简历</th>
                            <th>投递状态</th>
                            <th>移除</th>
                        </tr>
                        <tr v-for="(item, i) in tableData" :key="i">
                            <td><h1>{{ item.create_time | dateStr }}</h1></td>
                            <td><el-link :href="`/user/${item.user_id}`" target="_blank" :underline="false">{{ item.user__nic_name }}</el-link></td>
                            <td><el-link :href="`/position/${item.position_id}`" target="_blank" :underline="false">查看职位</el-link></td>
                            <td><el-link @click="checkResume(item.user__resume__id, item.pk)" :underline="false">查看简历</el-link></td>
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
        this.get_received_resume();
    },
    methods: {
        async get_received_resume () {
            let response = await this.axios.get(`${this.settings.Host}/received/user/${this.user_id}/`)
            this.tableData = response.data.data;
        },
        handleDelete(pk) {
            this.axios.get(`${this.settings.Host}/delivery/delete/${pk}/?type=receiver`)
            .then(res => {
                if (res.data.status == 200) {
                    this.get_received_resume()
                }
            }).catch(err => {
                console.log(err)
            })
        },
        checkResume (resume, pk) {
            this.$router.push(`/resume/${resume}`)
            this.axios.get(`${this.settings.Host}/received/change/${pk}/`)
        }
    }
}
</script>

<style lang="less" rel="stylesheet/less">
.received {
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