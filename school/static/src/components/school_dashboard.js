/** @odoo-module */

import { registry } from "@web/core/registry"
const {Component} = owl

export class SchoolDashboard extends Component{ Show usages

}

SchoolDashboard.template = "OwlSchoolDashboard"
registry.category("actions").add("school_dashboard", SchoolDashboard)