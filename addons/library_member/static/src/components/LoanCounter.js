// library_member/static/src/components/LoanCounter.js
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class LoanCounter extends Component {
    setup() {
        this.orm = useService("orm");
    }

    get loanCount() {
        return this.props.record.data.loan_count || 0;
    }

    onClick() {
        const count = this.loanCount;
        alert(`Este miembro tiene ${count} libro(s) prestado(s).`);
    }
}

LoanCounter.template = "library_member.LoanCounter";