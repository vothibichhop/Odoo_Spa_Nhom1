{
    'name': 'Quản lý khách hàng Spa',
    'version': '1.1.1',
    'category': 'Spa Management',
    'summary': 'Quản lý thông tin khách hàng Spa',
    'description': """
        Module quản lý khách hàng cho hệ thống Spa.
        Chức năng:
        - Mở rộng hồ sơ khách hàng Contact có sẵn của Odoo
        - Phân loại bằng Contact Tags; ghi chú và hoạt động qua chatter
        - Lưu nhu cầu chăm sóc, tình trạng da, sở thích và lưu ý
        - Theo dõi điểm bằng Odoo Loyalty và lịch sử liệu trình bằng lịch hẹn Spa
        - Tìm kiếm theo tên, điện thoại, email hoặc mã khách hàng
    """,
    'author': 'Spa ERP',
    'depends': [
        'contacts',
        'loyalty',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/customer_sequence.xml',
        'views/customer_views.xml',
        'views/customer_loyalty_views.xml',
        'views/customer_search_wizard_views.xml',
        'views/service_views.xml',
        'views/appointment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}