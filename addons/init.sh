# Navegar al directorio principal
cd library_member

# Crear archivos __init__.py en cada directorio necesario
touch __init__.py
touch models/__init__.py
touch views/__init__.py

# Crear __manifest__.py
cat > __manifest__.py << 'EOL'
{
    'name': 'Library Members',
    'version': '17.0.1.0.0',
    'category': 'Library',
    'summary': 'Manage library members',
    'description': """
        Manage library members and track book loans.
    """,
    'author': 'Tu Nombre',
    'website': 'https://www.tuwebsite.com',
    'depends': ['base', 'contacts'],
    'data': [
        'views/library_member_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'library_member/static/src/js/member_loan_count.js',
            'library_member/static/src/js/loan_count_widget.xml',
            'library_member/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
EOL

# Crear models/library_member.py
cat > models/library_member.py << 'EOL'
from odoo import models, fields, api

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        string='Related Partner',
        required=True,
        ondelete='cascade'
    )
    membership_number = fields.Char(
        string='Membership Number',
        required=True,
        default=lambda self: self._generate_membership_number()
    )
    join_date = fields.Date(
        string='Join Date',
        default=fields.Date.today()
    )
    loan_count = fields.Integer(
        string='Books Loaned',
        compute='_compute_loan_count',
        store=False
    )

    @api.model
    def _generate_membership_number(self):
        return self.env['ir.sequence'].next_by_code('library.member.sequence') or 'New'

    @api.depends('partner_id')
    def _compute_loan_count(self):
        # Esta función calcularía el número de libros prestados
        # Por ahora, usaremos un valor simulado para la demostración
        for member in self:
            member.loan_count = 5  # Valor de ejemplo

    @api.model
    def create(self, vals):
        if vals.get('membership_number', 'New') == 'New':
            vals['membership_number'] = self._generate_membership_number()
        return super().create(vals)
EOL

# Crear views/library_member_views.xml
cat > views/library_member_views.xml << 'EOL'
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Action para abrir la vista de miembros -->
    <record id="action_library_member" model="ir.actions.act_window">
        <field name="name">Library Members</field>
        <field name="res_model">library.member</field>
        <field name="view_mode">tree,form</field>
        <field name="context">{'default_is_company': False}</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create your first library member!
            </p>
        </field>
    </record>

    <!-- Menú principal -->
    <menuitem 
        id="menu_library_main" 
        name="Library" 
        sequence="10"/>
    
    <!-- Submenú para miembros -->
    <menuitem 
        id="menu_library_member" 
        name="Members" 
        parent="menu_library_main" 
        action="action_library_member" 
        sequence="10"/>

    <!-- Vista árbol -->
    <record id="view_library_member_tree" model="ir.ui.view">
        <field name="name">library.member.tree</field>
        <field name="model">library.member</field>
        <field name="arch" type="xml">
            <tree>
                <field name="membership_number"/>
                <field name="partner_id"/>
                <field name="join_date"/>
                <field name="loan_count"/>
            </tree>
        </field>
    </record>

    <!-- Vista formulario con componente OWL -->
    <record id="view_library_member_form" model="ir.ui.view">
        <field name="name">library.member.form</field>
        <field name="model">library.member</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <group>
                            <field name="membership_number"/>
                            <field name="partner_id" widget="res_partner_many2one"/>
                            <field name="join_date"/>
                        </group>
                        <group>
                            <!-- Componente OWL personalizado -->
                            <div class="oe_title">
                                <h1>
                                    <field name="name" readonly="1"/>
                                </h1>
                            </div>
                            <div class="o_stat_info">
                                <span class="o_stat_text">Books Loaned</span>
                                <field name="loan_count" widget="loan_count_widget"/>
                            </div>
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
EOL

# Crear security/ir.model.access.csv
cat > security/ir.model.access.csv << 'EOL'
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_member,library.member,model_library_member,,1,1,1,1
EOL

# Crear static/src/js/member_loan_count.js
cat > static/src/js/member_loan_count.js << 'EOL'
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
EOL

# Crear static/src/js/loan_count_widget.xml
cat > static/src/js/loan_count_widget.xml << 'EOL'
<?xml version="1.0" encoding="utf-8"?>
<templates xml:space="preserve">
    <t t-name="library_member.LoanCountWidget">
        <div class="o_loan_count_widget" t-on-click="onClick">
            <span class="o_loan_count_value" t-esc="state.loanCount"/>
            <span class="o_loan_count_label"> books on loan</span>
        </div>
    </t>
</templates>
EOL

# Crear static/src/css/style.css
cat > static/src/css/style.css << 'EOL'
.o_loan_count_widget {
    cursor: pointer;
    padding: 8px 12px;
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    display: inline-block;
    transition: background-color 0.3s;
}

.o_loan_count_widget:hover {
    background-color: #e9ecef;
}

.o_loan_count_value {
    font-size: 24px;
    font-weight: bold;
    color: #007bff;
}

.o_loan_count_label {
    font-size: 14px;
    color: #6c757d;
    margin-left: 8px;
}
EOL