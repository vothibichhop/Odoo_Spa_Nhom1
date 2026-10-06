{
    'name': 'Spa - Quản lý khách hàng',
    'version': '1.0',
    'category': 'Spa Management',
    'summary': 'Quản lý thông tin khách hàng Spa',
    'description': """
        Module quản lý khách hàng cho hệ thống Spa.
        Chức năng:
        - Quản lý thông tin khách hàng
        - Phân loại khách hàng
        - Quản lý lịch sử giao dịch
        - Theo dõi lịch sử chăm sóc
        - Quản lý điểm thành viên
        - Quản lý thông tin và nhu cầu khách hàng
        - Tìm kiếm và tra cứu khách hàng
    """,
    'author': 'Spa ERP',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/customer_search_wizard_views.xml',
        'views/service_views.xml',
        'views/appointment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}