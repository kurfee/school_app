/** @odoo-module */

import { registry } from "@web/core/registry"
import { KpiCard } from "./kpi_card/kpi_card"
import { ChartRenderer } from "./chart_renderer/chart_renderer"
import { loadJS } from "@web/core/assets"
import { useService } from "@web/core/utils/hooks"
const { Component, onWillStart, useRef, onMounted , useState } = owl

export class OwlSchoolDashboard extends Component {
    setup(){
        this.state = useState({
            student: {
                value:90,
                percentage:8,
            },
            period:90,
        })
        this.orm = useService("orm")

        onWillStart(async ()=>{
            await this.getStudent()
        })

    }
    onChangePeriod(){
        console.log(this.state.period)
    }

    async getStudent(){
        const data = await this.orm.searchCount("student.master", [['status','in',['active','draft']]])
        this.state.student.value= data
    }
}

OwlSchoolDashboard.template = "owl.OwlSchoolDashboard"
OwlSchoolDashboard.components = { KpiCard, ChartRenderer }

registry.category("actions").add("owl.school_dashboard", OwlSchoolDashboard)