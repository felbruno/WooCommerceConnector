{
 "creation": "2015-05-18 05:21:07.270859",
 "doctype": "DocType",
 "document_type": "System",
 "engine": "InnoDB",
 "field_order": [
  "status_html",
  "enable_woocommerce",
  "verify_ssl",
  "hourly_sync",
  "app_type",
  "column_break_4",
  "last_sync_datetime",
  "section_break_2",
  "woocommerce_url",
  "column_break_3",
  "api_key",
  "api_secret",
  "webhook_address",
  "access_token",
  "erp_settings",
  "price_list",
  "if_not_exists_create_item_to_woocommerce",
  "sync_items_from_woocommerce_to_erp",
  "sync_only_published",
  "sync_item_qty_from_erpnext_to_woocommerce",
  "default_item_group",
  "column_break_8",
  "default_customer",
  "customer_group",
  "item_code_based_on",
  "item_code_naming_series",
  "company_dependent_settings",
  "company",
  "cash_bank_account",
  "fee_account",
  "valuation_method",
  "column_break_20",
  "cost_center",
  "warehouse",
  "warehouses",
  "section_break_22",
  "weight_unit",
  "column_break_29",
  "dimensions_unit",
  "attribute_for_uom",
  "rewrite_stock_uom_from_wc_unit",
  "section_break_31",
  "html_16",
  "taxes",
  "section_tax_rules",
  "tax_rules",
  "section_break_25",
  "sales_order_series",
  "woocommerce_so_status",
  "column_break_27",
  "sync_delivery_note",
  "delivery_note_series",
  "sync_sales_invoice",
  "sales_invoice_series",
  "import_payment",
  "section_advanced",
  "sync_timeout",
  "trigger_update_item_stock"
 ],
 "fields": [
  {
   "fieldname": "status_html",
   "fieldtype": "HTML",
   "label": "status html",
   "read_only": 1
  },
  {
   "default": "1",
   "fieldname": "enable_woocommerce",
   "fieldtype": "Check",
   "label": "Enable woocommerce"
  },
  {
   "default": "0",
   "description": "Uncheck to run with self signed certificate",
   "fieldname": "verify_ssl",
   "fieldtype": "Check",
   "label": "Verify SSL"
  },
  {
   "default": "0",
   "fieldname": "hourly_sync",
   "fieldtype": "Check",
   "label": "Hourly synchronization"
  },
  {
   "default": "Public",
   "fieldname": "app_type",
   "fieldtype": "Select",
   "hidden": 1,
   "in_list_view": 1,
   "label": "App Type",
   "options": "Public\nPrivate",
   "reqd": 1
  },
  {
   "fieldname": "column_break_4",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "last_sync_datetime",
   "fieldtype": "Datetime",
   "label": "Last Sync Datetime",
   "read_only": 1
  },
  {
   "fieldname": "section_break_2",
   "fieldtype": "Section Break"
  },
  {
   "description": "eg: https://libracore.mywoocommerce.com",
   "fieldname": "woocommerce_url",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Shop URL",
   "reqd": 1
  },
  {
   "fieldname": "column_break_3",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "api_key",
   "fieldtype": "Data",
   "label": "API Key"
  },
  {
   "fieldname": "api_secret",
   "fieldtype": "Password",
   "label": "API Secret"
  },
  {
   "fieldname": "webhook_address",
   "fieldtype": "Data",
   "hidden": 1,
   "label": "Webhook Address"
  },
  {
   "fieldname": "access_token",
   "fieldtype": "Data",
   "hidden": 1,
   "label": "Access Token",
   "read_only": 1
  },
  {
   "fieldname": "erp_settings",
   "fieldtype": "Section Break"
  },
  {
   "description": "Sync Item Price, from seleted Price List with woocommerce",
   "fieldname": "price_list",
   "fieldtype": "Link",
   "label": "Price List",
   "options": "Price List"
  },
  {
   "default": "0",
   "fieldname": "if_not_exists_create_item_to_woocommerce",
   "fieldtype": "Check",
   "label": "If item does not exist, create item in woocommerce"
  },
  {
   "default": "0",
   "fieldname": "sync_items_from_woocommerce_to_erp",
   "fieldtype": "Check",
   "label": "Sync items from WooCommerce to ERPNext"
  },
  {
   "fieldname": "default_item_group",
   "fieldtype": "Link",
   "label": "Default Item Group",
   "options": "Item Group"
  },
  {
   "fieldname": "column_break_8",
   "fieldtype": "Column Break"
  },
  {
   "description": "If woocommerce not contains a customer in Order, then while syncing Orders, the system will consider default customer for order",
   "fieldname": "default_customer",
   "fieldtype": "Link",
   "label": "Default Customer",
   "options": "Customer"
  },
  {
   "description": "Customer Group will set to selected group while syncing customers from woocommerce",
   "fieldname": "customer_group",
   "fieldtype": "Link",
   "label": "Customer Group",
   "options": "Customer Group"
  },
  {
   "fieldname": "company_dependent_settings",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "company",
   "fieldtype": "Link",
   "label": "For Company",
   "options": "Company"
  },
  {
   "description": "Cash Account will used for Sales Invoice creation",
   "fieldname": "cash_bank_account",
   "fieldtype": "Link",
   "label": "Cash/Bank Account",
   "options": "Account"
  },
  {
   "fieldname": "fee_account",
   "fieldtype": "Link",
   "label": "Woocommerce Fee Account",
   "options": "Account",
   "reqd": 1
  },
  {
   "fieldname": "valuation_method",
   "fieldtype": "Select",
   "label": "Valuation Method",
   "options": "FIFO\nMoving Average",
   "reqd": 1
  },
  {
   "fieldname": "column_break_20",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "cost_center",
   "fieldtype": "Link",
   "label": "Cost Center",
   "options": "Cost Center"
  },
  {
   "description": "Sync Item Quantity, from seleted Warehouse with woocommerce",
   "fieldname": "warehouse",
   "fieldtype": "Link",
   "label": "Warehouse",
   "options": "Warehouse"
  },
  {
   "description": "To sync Item Quantity, from more than one Warehouse with woocommerce, use the following table (optionaly)",
   "fieldname": "warehouses",
   "fieldtype": "Table",
   "label": "Warehouses",
   "options": "WooWarehouses"
  },
  {
   "fieldname": "section_break_22",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "weight_unit",
   "fieldtype": "Link",
   "label": "Woocommerce Weight unit",
   "options": "UOM"
  },
  {
   "fieldname": "column_break_29",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "dimensions_unit",
   "fieldtype": "Link",
   "label": "Woocommerce Dimensions unit",
   "options": "UOM"
  },
  {
   "fieldname": "section_break_31",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "html_16",
   "fieldtype": "HTML",
   "options": "Map woocommerce Tax / Shipping to ERPNext Account"
  },
  {
   "fieldname": "taxes",
   "fieldtype": "Table",
   "label": "woocommerce Tax Account",
   "options": "woocommerce Tax Account"
  },
  {
   "fieldname": "section_tax_rules",
   "fieldtype": "Section Break",
   "label": "Tax Rules"
  },
  {
   "fieldname": "tax_rules",
   "fieldtype": "Table",
   "label": "Tax Rules",
   "options": "WooCommerce Tax Rule"
  },
  {
   "fieldname": "section_break_25",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "sales_order_series",
   "fieldtype": "Select",
   "label": "Sales Order Series"
  },
  {
   "fieldname": "column_break_27",
   "fieldtype": "Column Break"
  },
  {
   "default": "0",
   "fieldname": "sync_delivery_note",
   "fieldtype": "Check",
   "label": "Import Delivery Notes from woocommerce on Shipment"
  },
  {
   "depends_on": "eval:doc.sync_delivery_note==1",
   "fieldname": "delivery_note_series",
   "fieldtype": "Select",
   "label": "Delivery Note Series"
  },
  {
   "default": "0",
   "fieldname": "sync_sales_invoice",
   "fieldtype": "Check",
   "label": "Import Sales Invoice from woocommerce if Payment is marked"
  },
  {
   "depends_on": "eval:doc.sync_sales_invoice==1",
   "fieldname": "sales_invoice_series",
   "fieldtype": "Select",
   "label": "Sales Invoice Series"
  },
  {
   "default": "0",
   "depends_on": "eval:doc.sync_sales_invoice==1",
   "fieldname": "import_payment",
   "fieldtype": "Check",
   "label": "Import Payments"
  },
  {
   "fieldname": "section_advanced",
   "fieldtype": "Section Break",
   "label": "Advanced"
  },
  {
   "default": "1500",
   "description": "Timeout for sync background process",
   "fieldname": "sync_timeout",
   "fieldtype": "Int",
   "label": "Sync timeout"
  },
  {
   "default": "0",
   "depends_on": "eval:doc.sync_items_from_woocommerce_to_erp==1",
   "fieldname": "sync_item_qty_from_erpnext_to_woocommerce",
   "fieldtype": "Check",
   "label": "Sync item QTY from ERPNext to WooCommerce"
  },
  {
   "fieldname": "attribute_for_uom",
   "fieldtype": "Data",
   "label": "Attribute for UOM"
  },
  {
   "fieldname": "item_code_based_on",
   "fieldtype": "Select",
   "label": "Item code based on..",
   "options": "WooCommerce ID\nWooCommerce ID + Name\nWooCommerce Name\nRandom Hash\nNaming Series\nStock Keeping Unit",
   "reqd": 1
  },
  {
   "depends_on": "eval:doc.item_code_based_on=='Naming Series'",
   "fieldname": "item_code_naming_series",
   "fieldtype": "Select",
   "label": "Item code naming series"
  },
  {
   "default": "0",
   "fieldname": "rewrite_stock_uom_from_wc_unit",
   "fieldtype": "Check",
   "label": "rewrite stock uom from wc unit"
  },
  {
   "fieldname": "woocommerce_so_status",
   "fieldtype": "Table",
   "label": "WooCommerce SO Status for Import",
   "options": "WooCommerce SO Status"
  },
  {
   "default": "0",
   "fieldname": "trigger_update_item_stock",
   "fieldtype": "Check",
   "label": "Enable trigger to update item stock"
  },
  {
   "default": "0",
   "fieldname": "sync_only_published",
   "fieldtype": "Check",
   "label": "Only sync published items"
  }
 ],
 "issingle": 1,
 "modified": "2022-03-18 20:36:00.328416",
 "modified_by": "Administrator",
 "module": "WooCommerceConnector",
 "name": "WooCommerce Config",
 "owner": "Administrator",
 "permissions": [
  {
   "create": 1,
   "delete": 1,
   "email": 1,
   "print": 1,
   "read": 1,
   "role": "System Manager",
   "share": 1,
   "write": 1
  }
 ],
 "sort_field": "modified",
 "sort_order": "DESC"
}
