{
    'name' : 'Hospital Management System',
    'author' : 'Dhawal',
    'website' : 'www.dhawalksolves.com',
    'summary' : 'My first module',
    'Category' : 'A1',
    'depends': ['base', 'product', 'sale','hr'],
    'data' : [
        'security/ir.model.access.csv',
        # 'security/custom_security.xml',
        'security/security.xml',
        'wizard/patient_wizard_view.xml',
        'views/doctor.xml',
        'views/patient.xml',
        'views/bill.xml',
        'views/table.xml',
        'views/commands.xml',
        'views/menu.xml',
        'views/inherit_sale_order.xml',
        'views/hr_teacher_view.xml',
        'wizard/inherit_wizard.xml',
        'views/account_move_custom.xml',
        'reports/patient_report.xml',
        'reports/sale_report.xml'
    ]
}