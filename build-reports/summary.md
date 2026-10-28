## Dependency graph

**Build scenario:** `full`
**Changed products:** None
**Selected products (build order):** `thirdparty`, `catalog`, `customer`, `security`, `payment`, `orders`, `shipping`, `notification`, `reporting`

### Full-build dependency graph

```mermaid
flowchart LR
  subgraph Maven["Maven reactor modules"]
    m_thirdparty["thirdparty"]
    m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j["thirdparty/plugins/com.northwind.oms.tpcl.org.slf4j"]
    m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature["thirdparty/features/com.northwind.oms.tpcl.slf4j.feature"]
    m_catalog["catalog"]
    m_catalog_plugins_com_northwind_oms_core["catalog/plugins/com.northwind.oms.core"]
    m_catalog_plugins_com_northwind_oms_inventory["catalog/plugins/com.northwind.oms.inventory"]
    m_catalog_features_com_northwind_oms_catalog_feature["catalog/features/com.northwind.oms.catalog.feature"]
    m_customer["customer"]
    m_customer_plugins_com_northwind_oms_customer["customer/plugins/com.northwind.oms.customer"]
    m_customer_features_com_northwind_oms_customer_feature["customer/features/com.northwind.oms.customer.feature"]
    m_security["security"]
    m_security_plugins_com_northwind_oms_security["security/plugins/com.northwind.oms.security"]
    m_security_features_com_northwind_oms_security_feature["security/features/com.northwind.oms.security.feature"]
    m_payment["payment"]
    m_payment_plugins_com_northwind_oms_payment["payment/plugins/com.northwind.oms.payment"]
    m_payment_features_com_northwind_oms_payment_feature["payment/features/com.northwind.oms.payment.feature"]
    m_orders["orders"]
    m_orders_plugins_com_northwind_oms_pricing["orders/plugins/com.northwind.oms.pricing"]
    m_orders_plugins_com_northwind_oms_gateway["orders/plugins/com.northwind.oms.gateway"]
    m_orders_features_com_northwind_oms_orders_feature["orders/features/com.northwind.oms.orders.feature"]
    m_shipping["shipping"]
    m_shipping_plugins_com_northwind_oms_shipping["shipping/plugins/com.northwind.oms.shipping"]
    m_shipping_features_com_northwind_oms_shipping_feature["shipping/features/com.northwind.oms.shipping.feature"]
    m_notification["notification"]
    m_notification_plugins_com_northwind_oms_notification["notification/plugins/com.northwind.oms.notification"]
    m_notification_features_com_northwind_oms_notification_feature["notification/features/com.northwind.oms.notification.feature"]
    m_reporting["reporting"]
    m_reporting_plugins_com_northwind_oms_reporting["reporting/plugins/com.northwind.oms.reporting"]
    m_reporting_features_com_northwind_oms_reporting_feature["reporting/features/com.northwind.oms.reporting.feature"]
    m_thirdparty -->|contains-module| m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j
    m_thirdparty -->|contains-module| m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_core
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_inventory
    m_catalog -->|contains-module| m_catalog_features_com_northwind_oms_catalog_feature
    m_customer -->|contains-module| m_customer_plugins_com_northwind_oms_customer
    m_customer -->|contains-module| m_customer_features_com_northwind_oms_customer_feature
    m_security -->|contains-module| m_security_plugins_com_northwind_oms_security
    m_security -->|contains-module| m_security_features_com_northwind_oms_security_feature
    m_payment -->|contains-module| m_payment_plugins_com_northwind_oms_payment
    m_payment -->|contains-module| m_payment_features_com_northwind_oms_payment_feature
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_pricing
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_gateway
    m_orders -->|contains-module| m_orders_features_com_northwind_oms_orders_feature
    m_shipping -->|contains-module| m_shipping_plugins_com_northwind_oms_shipping
    m_shipping -->|contains-module| m_shipping_features_com_northwind_oms_shipping_feature
    m_notification -->|contains-module| m_notification_plugins_com_northwind_oms_notification
    m_notification -->|contains-module| m_notification_features_com_northwind_oms_notification_feature
    m_reporting -->|contains-module| m_reporting_plugins_com_northwind_oms_reporting
    m_reporting -->|contains-module| m_reporting_features_com_northwind_oms_reporting_feature
  end
  subgraph OSGi["OSGi bundles and features"]
    o_com_northwind_oms_core["com.northwind.oms.core"]
    o_com_northwind_oms_inventory["com.northwind.oms.inventory"]
    o_com_northwind_oms_customer["com.northwind.oms.customer"]
    o_com_northwind_oms_notification["com.northwind.oms.notification"]
    o_com_northwind_oms_gateway["com.northwind.oms.gateway"]
    o_com_northwind_oms_pricing["com.northwind.oms.pricing"]
    o_com_northwind_oms_payment["com.northwind.oms.payment"]
    o_com_northwind_oms_reporting["com.northwind.oms.reporting"]
    o_com_northwind_oms_security["com.northwind.oms.security"]
    o_com_northwind_oms_shipping["com.northwind.oms.shipping"]
    o_com_northwind_oms_tpcl_org_slf4j["com.northwind.oms.tpcl.org.slf4j"]
    f_com_northwind_oms_catalog_feature(["com.northwind.oms.catalog.feature"])
    f_com_northwind_oms_customer_feature(["com.northwind.oms.customer.feature"])
    f_com_northwind_oms_notification_feature(["com.northwind.oms.notification.feature"])
    f_com_northwind_oms_orders_feature(["com.northwind.oms.orders.feature"])
    f_com_northwind_oms_payment_feature(["com.northwind.oms.payment.feature"])
    f_com_northwind_oms_reporting_feature(["com.northwind.oms.reporting.feature"])
    f_com_northwind_oms_security_feature(["com.northwind.oms.security.feature"])
    f_com_northwind_oms_shipping_feature(["com.northwind.oms.shipping.feature"])
    f_com_northwind_oms_tpcl_slf4j_feature(["com.northwind.oms.tpcl.slf4j.feature"])
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_customer
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_shipping
    o_com_northwind_oms_notification -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_inventory
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_pricing
    o_com_northwind_oms_gateway -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_security
    o_com_northwind_oms_payment -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_payment
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_gateway
    o_com_northwind_oms_reporting -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_customer
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_core
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_inventory
    f_com_northwind_oms_customer_feature -->|contains-bundle| o_com_northwind_oms_customer
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_shipping_feature
    f_com_northwind_oms_notification_feature -->|contains-bundle| o_com_northwind_oms_notification
    f_com_northwind_oms_orders_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_pricing
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_gateway
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_security_feature
    f_com_northwind_oms_payment_feature -->|contains-bundle| o_com_northwind_oms_payment
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_orders_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_payment_feature
    f_com_northwind_oms_reporting_feature -->|contains-bundle| o_com_northwind_oms_reporting
    f_com_northwind_oms_security_feature -->|contains-bundle| o_com_northwind_oms_security
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_shipping_feature -->|contains-bundle| o_com_northwind_oms_shipping
    f_com_northwind_oms_tpcl_slf4j_feature -->|contains-bundle| o_com_northwind_oms_tpcl_org_slf4j
  end
```

### Changed-products dependency graph

```mermaid
flowchart LR
  subgraph Maven["Maven reactor modules"]
    m_thirdparty["thirdparty"]
    m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j["thirdparty/plugins/com.northwind.oms.tpcl.org.slf4j"]
    m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature["thirdparty/features/com.northwind.oms.tpcl.slf4j.feature"]
    m_catalog["catalog"]
    m_catalog_plugins_com_northwind_oms_core["catalog/plugins/com.northwind.oms.core"]
    m_catalog_plugins_com_northwind_oms_inventory["catalog/plugins/com.northwind.oms.inventory"]
    m_catalog_features_com_northwind_oms_catalog_feature["catalog/features/com.northwind.oms.catalog.feature"]
    m_customer["customer"]
    m_customer_plugins_com_northwind_oms_customer["customer/plugins/com.northwind.oms.customer"]
    m_customer_features_com_northwind_oms_customer_feature["customer/features/com.northwind.oms.customer.feature"]
    m_security["security"]
    m_security_plugins_com_northwind_oms_security["security/plugins/com.northwind.oms.security"]
    m_security_features_com_northwind_oms_security_feature["security/features/com.northwind.oms.security.feature"]
    m_payment["payment"]
    m_payment_plugins_com_northwind_oms_payment["payment/plugins/com.northwind.oms.payment"]
    m_payment_features_com_northwind_oms_payment_feature["payment/features/com.northwind.oms.payment.feature"]
    m_orders["orders"]
    m_orders_plugins_com_northwind_oms_pricing["orders/plugins/com.northwind.oms.pricing"]
    m_orders_plugins_com_northwind_oms_gateway["orders/plugins/com.northwind.oms.gateway"]
    m_orders_features_com_northwind_oms_orders_feature["orders/features/com.northwind.oms.orders.feature"]
    m_shipping["shipping"]
    m_shipping_plugins_com_northwind_oms_shipping["shipping/plugins/com.northwind.oms.shipping"]
    m_shipping_features_com_northwind_oms_shipping_feature["shipping/features/com.northwind.oms.shipping.feature"]
    m_notification["notification"]
    m_notification_plugins_com_northwind_oms_notification["notification/plugins/com.northwind.oms.notification"]
    m_notification_features_com_northwind_oms_notification_feature["notification/features/com.northwind.oms.notification.feature"]
    m_reporting["reporting"]
    m_reporting_plugins_com_northwind_oms_reporting["reporting/plugins/com.northwind.oms.reporting"]
    m_reporting_features_com_northwind_oms_reporting_feature["reporting/features/com.northwind.oms.reporting.feature"]
    m_thirdparty -->|contains-module| m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j
    m_thirdparty -->|contains-module| m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_core
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_inventory
    m_catalog -->|contains-module| m_catalog_features_com_northwind_oms_catalog_feature
    m_customer -->|contains-module| m_customer_plugins_com_northwind_oms_customer
    m_customer -->|contains-module| m_customer_features_com_northwind_oms_customer_feature
    m_security -->|contains-module| m_security_plugins_com_northwind_oms_security
    m_security -->|contains-module| m_security_features_com_northwind_oms_security_feature
    m_payment -->|contains-module| m_payment_plugins_com_northwind_oms_payment
    m_payment -->|contains-module| m_payment_features_com_northwind_oms_payment_feature
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_pricing
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_gateway
    m_orders -->|contains-module| m_orders_features_com_northwind_oms_orders_feature
    m_shipping -->|contains-module| m_shipping_plugins_com_northwind_oms_shipping
    m_shipping -->|contains-module| m_shipping_features_com_northwind_oms_shipping_feature
    m_notification -->|contains-module| m_notification_plugins_com_northwind_oms_notification
    m_notification -->|contains-module| m_notification_features_com_northwind_oms_notification_feature
    m_reporting -->|contains-module| m_reporting_plugins_com_northwind_oms_reporting
    m_reporting -->|contains-module| m_reporting_features_com_northwind_oms_reporting_feature
  end
  subgraph Impact["Changed-product impact paths"]
    p_thirdparty["thirdparty (selected)"]
    p_catalog["catalog (selected)"]
    p_customer["customer (selected)"]
    p_security["security (selected)"]
    p_payment["payment (selected)"]
    p_orders["orders (selected)"]
    p_shipping["shipping (selected)"]
    p_notification["notification (selected)"]
    p_reporting["reporting (selected)"]
    p_catalog -->|dependency| p_payment
    p_security -->|dependency| p_payment
    p_thirdparty -->|dependency| p_payment
    p_catalog -->|dependency| p_orders
    p_thirdparty -->|dependency| p_orders
    p_catalog -->|dependency| p_shipping
    p_customer -->|dependency| p_shipping
    p_customer -->|dependency| p_notification
    p_shipping -->|dependency| p_notification
    p_thirdparty -->|dependency| p_notification
    p_catalog -->|dependency| p_reporting
    p_orders -->|dependency| p_reporting
    p_payment -->|dependency| p_reporting
    p_thirdparty -->|dependency| p_reporting
  end
  subgraph OSGi["OSGi bundles and features"]
    o_com_northwind_oms_core["com.northwind.oms.core"]
    o_com_northwind_oms_inventory["com.northwind.oms.inventory"]
    o_com_northwind_oms_customer["com.northwind.oms.customer"]
    o_com_northwind_oms_notification["com.northwind.oms.notification"]
    o_com_northwind_oms_gateway["com.northwind.oms.gateway"]
    o_com_northwind_oms_pricing["com.northwind.oms.pricing"]
    o_com_northwind_oms_payment["com.northwind.oms.payment"]
    o_com_northwind_oms_reporting["com.northwind.oms.reporting"]
    o_com_northwind_oms_security["com.northwind.oms.security"]
    o_com_northwind_oms_shipping["com.northwind.oms.shipping"]
    o_com_northwind_oms_tpcl_org_slf4j["com.northwind.oms.tpcl.org.slf4j"]
    f_com_northwind_oms_catalog_feature(["com.northwind.oms.catalog.feature"])
    f_com_northwind_oms_customer_feature(["com.northwind.oms.customer.feature"])
    f_com_northwind_oms_notification_feature(["com.northwind.oms.notification.feature"])
    f_com_northwind_oms_orders_feature(["com.northwind.oms.orders.feature"])
    f_com_northwind_oms_payment_feature(["com.northwind.oms.payment.feature"])
    f_com_northwind_oms_reporting_feature(["com.northwind.oms.reporting.feature"])
    f_com_northwind_oms_security_feature(["com.northwind.oms.security.feature"])
    f_com_northwind_oms_shipping_feature(["com.northwind.oms.shipping.feature"])
    f_com_northwind_oms_tpcl_slf4j_feature(["com.northwind.oms.tpcl.slf4j.feature"])
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_customer
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_shipping
    o_com_northwind_oms_notification -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_inventory
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_pricing
    o_com_northwind_oms_gateway -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_security
    o_com_northwind_oms_payment -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_payment
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_gateway
    o_com_northwind_oms_reporting -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_customer
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_core
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_inventory
    f_com_northwind_oms_customer_feature -->|contains-bundle| o_com_northwind_oms_customer
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_shipping_feature
    f_com_northwind_oms_notification_feature -->|contains-bundle| o_com_northwind_oms_notification
    f_com_northwind_oms_orders_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_pricing
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_gateway
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_security_feature
    f_com_northwind_oms_payment_feature -->|contains-bundle| o_com_northwind_oms_payment
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_orders_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_payment_feature
    f_com_northwind_oms_reporting_feature -->|contains-bundle| o_com_northwind_oms_reporting
    f_com_northwind_oms_security_feature -->|contains-bundle| o_com_northwind_oms_security
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_shipping_feature -->|contains-bundle| o_com_northwind_oms_shipping
    f_com_northwind_oms_tpcl_slf4j_feature -->|contains-bundle| o_com_northwind_oms_tpcl_org_slf4j
  end
  classDef selected fill:#d1fae5,stroke:#059669,stroke-width:2px
  classDef changed fill:#fef3c7,stroke:#d97706,stroke-width:3px
  class m_catalog selected
  class m_catalog_plugins_com_northwind_oms_core selected
  class m_catalog_plugins_com_northwind_oms_inventory selected
  class m_catalog_features_com_northwind_oms_catalog_feature selected
  class o_com_northwind_oms_core selected
  class o_com_northwind_oms_inventory selected
  class f_com_northwind_oms_catalog_feature selected
  class m_customer selected
  class m_customer_plugins_com_northwind_oms_customer selected
  class m_customer_features_com_northwind_oms_customer_feature selected
  class o_com_northwind_oms_customer selected
  class f_com_northwind_oms_customer_feature selected
  class m_notification selected
  class m_notification_plugins_com_northwind_oms_notification selected
  class m_notification_features_com_northwind_oms_notification_feature selected
  class o_com_northwind_oms_notification selected
  class f_com_northwind_oms_notification_feature selected
  class m_orders selected
  class m_orders_plugins_com_northwind_oms_pricing selected
  class m_orders_plugins_com_northwind_oms_gateway selected
  class m_orders_features_com_northwind_oms_orders_feature selected
  class o_com_northwind_oms_gateway selected
  class o_com_northwind_oms_pricing selected
  class f_com_northwind_oms_orders_feature selected
  class m_payment selected
  class m_payment_plugins_com_northwind_oms_payment selected
  class m_payment_features_com_northwind_oms_payment_feature selected
  class o_com_northwind_oms_payment selected
  class f_com_northwind_oms_payment_feature selected
  class m_reporting selected
  class m_reporting_plugins_com_northwind_oms_reporting selected
  class m_reporting_features_com_northwind_oms_reporting_feature selected
  class o_com_northwind_oms_reporting selected
  class f_com_northwind_oms_reporting_feature selected
  class m_security selected
  class m_security_plugins_com_northwind_oms_security selected
  class m_security_features_com_northwind_oms_security_feature selected
  class o_com_northwind_oms_security selected
  class f_com_northwind_oms_security_feature selected
  class m_shipping selected
  class m_shipping_plugins_com_northwind_oms_shipping selected
  class m_shipping_features_com_northwind_oms_shipping_feature selected
  class o_com_northwind_oms_shipping selected
  class f_com_northwind_oms_shipping_feature selected
  class m_thirdparty selected
  class m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j selected
  class m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature selected
  class o_com_northwind_oms_tpcl_org_slf4j selected
  class f_com_northwind_oms_tpcl_slf4j_feature selected
```
## Dependency graph

**Build scenario:** `changed`
**Changed products:** `catalog`
**Selected products (build order):** `thirdparty`, `catalog`, `customer`, `security`, `payment`, `orders`, `shipping`, `notification`, `reporting`

### Dependency impact paths

- **catalog:** `catalog -> orders`; `catalog -> payment`; `catalog -> reporting`; `catalog -> shipping`; `catalog -> orders -> reporting`; `catalog -> payment -> reporting`; `catalog -> shipping -> notification`

### Full-build dependency graph

```mermaid
flowchart LR
  subgraph Maven["Maven reactor modules"]
    m_thirdparty["thirdparty"]
    m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j["thirdparty/plugins/com.northwind.oms.tpcl.org.slf4j"]
    m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature["thirdparty/features/com.northwind.oms.tpcl.slf4j.feature"]
    m_catalog["catalog"]
    m_catalog_plugins_com_northwind_oms_core["catalog/plugins/com.northwind.oms.core"]
    m_catalog_plugins_com_northwind_oms_inventory["catalog/plugins/com.northwind.oms.inventory"]
    m_catalog_features_com_northwind_oms_catalog_feature["catalog/features/com.northwind.oms.catalog.feature"]
    m_customer["customer"]
    m_customer_plugins_com_northwind_oms_customer["customer/plugins/com.northwind.oms.customer"]
    m_customer_features_com_northwind_oms_customer_feature["customer/features/com.northwind.oms.customer.feature"]
    m_security["security"]
    m_security_plugins_com_northwind_oms_security["security/plugins/com.northwind.oms.security"]
    m_security_features_com_northwind_oms_security_feature["security/features/com.northwind.oms.security.feature"]
    m_payment["payment"]
    m_payment_plugins_com_northwind_oms_payment["payment/plugins/com.northwind.oms.payment"]
    m_payment_features_com_northwind_oms_payment_feature["payment/features/com.northwind.oms.payment.feature"]
    m_orders["orders"]
    m_orders_plugins_com_northwind_oms_pricing["orders/plugins/com.northwind.oms.pricing"]
    m_orders_plugins_com_northwind_oms_gateway["orders/plugins/com.northwind.oms.gateway"]
    m_orders_features_com_northwind_oms_orders_feature["orders/features/com.northwind.oms.orders.feature"]
    m_shipping["shipping"]
    m_shipping_plugins_com_northwind_oms_shipping["shipping/plugins/com.northwind.oms.shipping"]
    m_shipping_features_com_northwind_oms_shipping_feature["shipping/features/com.northwind.oms.shipping.feature"]
    m_notification["notification"]
    m_notification_plugins_com_northwind_oms_notification["notification/plugins/com.northwind.oms.notification"]
    m_notification_features_com_northwind_oms_notification_feature["notification/features/com.northwind.oms.notification.feature"]
    m_reporting["reporting"]
    m_reporting_plugins_com_northwind_oms_reporting["reporting/plugins/com.northwind.oms.reporting"]
    m_reporting_features_com_northwind_oms_reporting_feature["reporting/features/com.northwind.oms.reporting.feature"]
    m_thirdparty -->|contains-module| m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j
    m_thirdparty -->|contains-module| m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_core
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_inventory
    m_catalog -->|contains-module| m_catalog_features_com_northwind_oms_catalog_feature
    m_customer -->|contains-module| m_customer_plugins_com_northwind_oms_customer
    m_customer -->|contains-module| m_customer_features_com_northwind_oms_customer_feature
    m_security -->|contains-module| m_security_plugins_com_northwind_oms_security
    m_security -->|contains-module| m_security_features_com_northwind_oms_security_feature
    m_payment -->|contains-module| m_payment_plugins_com_northwind_oms_payment
    m_payment -->|contains-module| m_payment_features_com_northwind_oms_payment_feature
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_pricing
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_gateway
    m_orders -->|contains-module| m_orders_features_com_northwind_oms_orders_feature
    m_shipping -->|contains-module| m_shipping_plugins_com_northwind_oms_shipping
    m_shipping -->|contains-module| m_shipping_features_com_northwind_oms_shipping_feature
    m_notification -->|contains-module| m_notification_plugins_com_northwind_oms_notification
    m_notification -->|contains-module| m_notification_features_com_northwind_oms_notification_feature
    m_reporting -->|contains-module| m_reporting_plugins_com_northwind_oms_reporting
    m_reporting -->|contains-module| m_reporting_features_com_northwind_oms_reporting_feature
  end
  subgraph OSGi["OSGi bundles and features"]
    o_com_northwind_oms_core["com.northwind.oms.core"]
    o_com_northwind_oms_inventory["com.northwind.oms.inventory"]
    o_com_northwind_oms_customer["com.northwind.oms.customer"]
    o_com_northwind_oms_notification["com.northwind.oms.notification"]
    o_com_northwind_oms_gateway["com.northwind.oms.gateway"]
    o_com_northwind_oms_pricing["com.northwind.oms.pricing"]
    o_com_northwind_oms_payment["com.northwind.oms.payment"]
    o_com_northwind_oms_reporting["com.northwind.oms.reporting"]
    o_com_northwind_oms_security["com.northwind.oms.security"]
    o_com_northwind_oms_shipping["com.northwind.oms.shipping"]
    o_com_northwind_oms_tpcl_org_slf4j["com.northwind.oms.tpcl.org.slf4j"]
    f_com_northwind_oms_catalog_feature(["com.northwind.oms.catalog.feature"])
    f_com_northwind_oms_customer_feature(["com.northwind.oms.customer.feature"])
    f_com_northwind_oms_notification_feature(["com.northwind.oms.notification.feature"])
    f_com_northwind_oms_orders_feature(["com.northwind.oms.orders.feature"])
    f_com_northwind_oms_payment_feature(["com.northwind.oms.payment.feature"])
    f_com_northwind_oms_reporting_feature(["com.northwind.oms.reporting.feature"])
    f_com_northwind_oms_security_feature(["com.northwind.oms.security.feature"])
    f_com_northwind_oms_shipping_feature(["com.northwind.oms.shipping.feature"])
    f_com_northwind_oms_tpcl_slf4j_feature(["com.northwind.oms.tpcl.slf4j.feature"])
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_customer
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_shipping
    o_com_northwind_oms_notification -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_inventory
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_pricing
    o_com_northwind_oms_gateway -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_security
    o_com_northwind_oms_payment -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_payment
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_gateway
    o_com_northwind_oms_reporting -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_customer
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_core
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_inventory
    f_com_northwind_oms_customer_feature -->|contains-bundle| o_com_northwind_oms_customer
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_shipping_feature
    f_com_northwind_oms_notification_feature -->|contains-bundle| o_com_northwind_oms_notification
    f_com_northwind_oms_orders_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_pricing
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_gateway
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_security_feature
    f_com_northwind_oms_payment_feature -->|contains-bundle| o_com_northwind_oms_payment
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_orders_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_payment_feature
    f_com_northwind_oms_reporting_feature -->|contains-bundle| o_com_northwind_oms_reporting
    f_com_northwind_oms_security_feature -->|contains-bundle| o_com_northwind_oms_security
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_shipping_feature -->|contains-bundle| o_com_northwind_oms_shipping
    f_com_northwind_oms_tpcl_slf4j_feature -->|contains-bundle| o_com_northwind_oms_tpcl_org_slf4j
  end
```

### Changed-products dependency graph

```mermaid
flowchart LR
  subgraph Maven["Maven reactor modules"]
    m_thirdparty["thirdparty"]
    m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j["thirdparty/plugins/com.northwind.oms.tpcl.org.slf4j"]
    m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature["thirdparty/features/com.northwind.oms.tpcl.slf4j.feature"]
    m_catalog["catalog"]
    m_catalog_plugins_com_northwind_oms_core["catalog/plugins/com.northwind.oms.core"]
    m_catalog_plugins_com_northwind_oms_inventory["catalog/plugins/com.northwind.oms.inventory"]
    m_catalog_features_com_northwind_oms_catalog_feature["catalog/features/com.northwind.oms.catalog.feature"]
    m_customer["customer"]
    m_customer_plugins_com_northwind_oms_customer["customer/plugins/com.northwind.oms.customer"]
    m_customer_features_com_northwind_oms_customer_feature["customer/features/com.northwind.oms.customer.feature"]
    m_security["security"]
    m_security_plugins_com_northwind_oms_security["security/plugins/com.northwind.oms.security"]
    m_security_features_com_northwind_oms_security_feature["security/features/com.northwind.oms.security.feature"]
    m_payment["payment"]
    m_payment_plugins_com_northwind_oms_payment["payment/plugins/com.northwind.oms.payment"]
    m_payment_features_com_northwind_oms_payment_feature["payment/features/com.northwind.oms.payment.feature"]
    m_orders["orders"]
    m_orders_plugins_com_northwind_oms_pricing["orders/plugins/com.northwind.oms.pricing"]
    m_orders_plugins_com_northwind_oms_gateway["orders/plugins/com.northwind.oms.gateway"]
    m_orders_features_com_northwind_oms_orders_feature["orders/features/com.northwind.oms.orders.feature"]
    m_shipping["shipping"]
    m_shipping_plugins_com_northwind_oms_shipping["shipping/plugins/com.northwind.oms.shipping"]
    m_shipping_features_com_northwind_oms_shipping_feature["shipping/features/com.northwind.oms.shipping.feature"]
    m_notification["notification"]
    m_notification_plugins_com_northwind_oms_notification["notification/plugins/com.northwind.oms.notification"]
    m_notification_features_com_northwind_oms_notification_feature["notification/features/com.northwind.oms.notification.feature"]
    m_reporting["reporting"]
    m_reporting_plugins_com_northwind_oms_reporting["reporting/plugins/com.northwind.oms.reporting"]
    m_reporting_features_com_northwind_oms_reporting_feature["reporting/features/com.northwind.oms.reporting.feature"]
    m_thirdparty -->|contains-module| m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j
    m_thirdparty -->|contains-module| m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_core
    m_catalog -->|contains-module| m_catalog_plugins_com_northwind_oms_inventory
    m_catalog -->|contains-module| m_catalog_features_com_northwind_oms_catalog_feature
    m_customer -->|contains-module| m_customer_plugins_com_northwind_oms_customer
    m_customer -->|contains-module| m_customer_features_com_northwind_oms_customer_feature
    m_security -->|contains-module| m_security_plugins_com_northwind_oms_security
    m_security -->|contains-module| m_security_features_com_northwind_oms_security_feature
    m_payment -->|contains-module| m_payment_plugins_com_northwind_oms_payment
    m_payment -->|contains-module| m_payment_features_com_northwind_oms_payment_feature
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_pricing
    m_orders -->|contains-module| m_orders_plugins_com_northwind_oms_gateway
    m_orders -->|contains-module| m_orders_features_com_northwind_oms_orders_feature
    m_shipping -->|contains-module| m_shipping_plugins_com_northwind_oms_shipping
    m_shipping -->|contains-module| m_shipping_features_com_northwind_oms_shipping_feature
    m_notification -->|contains-module| m_notification_plugins_com_northwind_oms_notification
    m_notification -->|contains-module| m_notification_features_com_northwind_oms_notification_feature
    m_reporting -->|contains-module| m_reporting_plugins_com_northwind_oms_reporting
    m_reporting -->|contains-module| m_reporting_features_com_northwind_oms_reporting_feature
  end
  subgraph Impact["Changed-product impact paths"]
    p_thirdparty["thirdparty (selected)"]
    p_catalog["catalog (selected)"]
    p_customer["customer (selected)"]
    p_security["security (selected)"]
    p_payment["payment (selected)"]
    p_orders["orders (selected)"]
    p_shipping["shipping (selected)"]
    p_notification["notification (selected)"]
    p_reporting["reporting (selected)"]
    p_catalog -->|dependency| p_payment
    p_security -->|dependency| p_payment
    p_thirdparty -->|dependency| p_payment
    p_catalog -->|dependency| p_orders
    p_thirdparty -->|dependency| p_orders
    p_catalog -->|dependency| p_shipping
    p_customer -->|dependency| p_shipping
    p_customer -->|dependency| p_notification
    p_shipping -->|dependency| p_notification
    p_thirdparty -->|dependency| p_notification
    p_catalog -->|dependency| p_reporting
    p_orders -->|dependency| p_reporting
    p_payment -->|dependency| p_reporting
    p_thirdparty -->|dependency| p_reporting
    p_catalog:::changed
  end
  subgraph OSGi["OSGi bundles and features"]
    o_com_northwind_oms_core["com.northwind.oms.core"]
    o_com_northwind_oms_inventory["com.northwind.oms.inventory"]
    o_com_northwind_oms_customer["com.northwind.oms.customer"]
    o_com_northwind_oms_notification["com.northwind.oms.notification"]
    o_com_northwind_oms_gateway["com.northwind.oms.gateway"]
    o_com_northwind_oms_pricing["com.northwind.oms.pricing"]
    o_com_northwind_oms_payment["com.northwind.oms.payment"]
    o_com_northwind_oms_reporting["com.northwind.oms.reporting"]
    o_com_northwind_oms_security["com.northwind.oms.security"]
    o_com_northwind_oms_shipping["com.northwind.oms.shipping"]
    o_com_northwind_oms_tpcl_org_slf4j["com.northwind.oms.tpcl.org.slf4j"]
    f_com_northwind_oms_catalog_feature(["com.northwind.oms.catalog.feature"])
    f_com_northwind_oms_customer_feature(["com.northwind.oms.customer.feature"])
    f_com_northwind_oms_notification_feature(["com.northwind.oms.notification.feature"])
    f_com_northwind_oms_orders_feature(["com.northwind.oms.orders.feature"])
    f_com_northwind_oms_payment_feature(["com.northwind.oms.payment.feature"])
    f_com_northwind_oms_reporting_feature(["com.northwind.oms.reporting.feature"])
    f_com_northwind_oms_security_feature(["com.northwind.oms.security.feature"])
    f_com_northwind_oms_shipping_feature(["com.northwind.oms.shipping.feature"])
    f_com_northwind_oms_tpcl_slf4j_feature(["com.northwind.oms.tpcl.slf4j.feature"])
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_inventory -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_customer
    o_com_northwind_oms_notification -->|imports-package| o_com_northwind_oms_shipping
    o_com_northwind_oms_notification -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_inventory
    o_com_northwind_oms_gateway -->|imports-package| o_com_northwind_oms_pricing
    o_com_northwind_oms_gateway -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_pricing -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_payment -->|imports-package| o_com_northwind_oms_security
    o_com_northwind_oms_payment -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_payment
    o_com_northwind_oms_reporting -->|imports-package| o_com_northwind_oms_gateway
    o_com_northwind_oms_reporting -->|requires-bundle| o_com_northwind_oms_tpcl_org_slf4j
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_core
    o_com_northwind_oms_shipping -->|imports-package| o_com_northwind_oms_customer
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_core
    f_com_northwind_oms_catalog_feature -->|contains-bundle| o_com_northwind_oms_inventory
    f_com_northwind_oms_customer_feature -->|contains-bundle| o_com_northwind_oms_customer
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_notification_feature -->|requires-feature| f_com_northwind_oms_shipping_feature
    f_com_northwind_oms_notification_feature -->|contains-bundle| o_com_northwind_oms_notification
    f_com_northwind_oms_orders_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_pricing
    f_com_northwind_oms_orders_feature -->|contains-bundle| o_com_northwind_oms_gateway
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_payment_feature -->|requires-feature| f_com_northwind_oms_security_feature
    f_com_northwind_oms_payment_feature -->|contains-bundle| o_com_northwind_oms_payment
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_orders_feature
    f_com_northwind_oms_reporting_feature -->|requires-feature| f_com_northwind_oms_payment_feature
    f_com_northwind_oms_reporting_feature -->|contains-bundle| o_com_northwind_oms_reporting
    f_com_northwind_oms_security_feature -->|contains-bundle| o_com_northwind_oms_security
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_catalog_feature
    f_com_northwind_oms_shipping_feature -->|requires-feature| f_com_northwind_oms_customer_feature
    f_com_northwind_oms_shipping_feature -->|contains-bundle| o_com_northwind_oms_shipping
    f_com_northwind_oms_tpcl_slf4j_feature -->|contains-bundle| o_com_northwind_oms_tpcl_org_slf4j
  end
  classDef selected fill:#d1fae5,stroke:#059669,stroke-width:2px
  classDef changed fill:#fef3c7,stroke:#d97706,stroke-width:3px
  class m_catalog selected
  class m_catalog_plugins_com_northwind_oms_core selected
  class m_catalog_plugins_com_northwind_oms_inventory selected
  class m_catalog_features_com_northwind_oms_catalog_feature selected
  class o_com_northwind_oms_core selected
  class o_com_northwind_oms_inventory selected
  class f_com_northwind_oms_catalog_feature selected
  class m_customer selected
  class m_customer_plugins_com_northwind_oms_customer selected
  class m_customer_features_com_northwind_oms_customer_feature selected
  class o_com_northwind_oms_customer selected
  class f_com_northwind_oms_customer_feature selected
  class m_notification selected
  class m_notification_plugins_com_northwind_oms_notification selected
  class m_notification_features_com_northwind_oms_notification_feature selected
  class o_com_northwind_oms_notification selected
  class f_com_northwind_oms_notification_feature selected
  class m_orders selected
  class m_orders_plugins_com_northwind_oms_pricing selected
  class m_orders_plugins_com_northwind_oms_gateway selected
  class m_orders_features_com_northwind_oms_orders_feature selected
  class o_com_northwind_oms_gateway selected
  class o_com_northwind_oms_pricing selected
  class f_com_northwind_oms_orders_feature selected
  class m_payment selected
  class m_payment_plugins_com_northwind_oms_payment selected
  class m_payment_features_com_northwind_oms_payment_feature selected
  class o_com_northwind_oms_payment selected
  class f_com_northwind_oms_payment_feature selected
  class m_reporting selected
  class m_reporting_plugins_com_northwind_oms_reporting selected
  class m_reporting_features_com_northwind_oms_reporting_feature selected
  class o_com_northwind_oms_reporting selected
  class f_com_northwind_oms_reporting_feature selected
  class m_security selected
  class m_security_plugins_com_northwind_oms_security selected
  class m_security_features_com_northwind_oms_security_feature selected
  class o_com_northwind_oms_security selected
  class f_com_northwind_oms_security_feature selected
  class m_shipping selected
  class m_shipping_plugins_com_northwind_oms_shipping selected
  class m_shipping_features_com_northwind_oms_shipping_feature selected
  class o_com_northwind_oms_shipping selected
  class f_com_northwind_oms_shipping_feature selected
  class m_thirdparty selected
  class m_thirdparty_plugins_com_northwind_oms_tpcl_org_slf4j selected
  class m_thirdparty_features_com_northwind_oms_tpcl_slf4j_feature selected
  class o_com_northwind_oms_tpcl_org_slf4j selected
  class f_com_northwind_oms_tpcl_slf4j_feature selected
  class p_catalog changed
```
