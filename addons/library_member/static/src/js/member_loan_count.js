odoo.define('library_member.LoanCountWidget', function (require) {
    "use strict";

    const { Component } = owl;
    const { useState, onMounted } = owl.hooks;
    const fieldRegistry = require('web.field_registry');
    const AbstractField = require('web.AbstractField');

    // Componente OWL
    class LoanCountWidget extends AbstractField {
        constructor() {
            super(...arguments);
            this.state = useState({
                loanCount: this.value || 0,
            });
        }

        // Cuando se hace clic en el componente
        onClick() {
            alert(`This member has ${this.state.loanCount} books on loan!`);
        }

        // Actualizar cuando cambia el valor
        _render() {
            this.state.loanCount = this.value;
        }
    }

    // Template del componente
    LoanCountWidget.template = 'library_member.LoanCountWidget';
    LoanCountWidget.props = {
        ...AbstractField.props,
    };

    // Registrar el widget
    fieldRegistry.add('loan_count_widget', LoanCountWidget);

    return LoanCountWidget;
});
