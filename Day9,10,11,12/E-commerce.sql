Table categories {
  category_id integer [pk]
  category_name varchar(255)
  description varchar(255)
}

Table customers {
  customer_id integer [pk]
  customer_name varchar(255)
  contact_name varchar(255)
  address varchar(255)
  city varchar(255)
  postal_code varchar(255)
  country varchar(255)
}

Table orders {
  order_id integer [pk]
  customer_id integer
  order_date date
}

Table order_details {
  order_detail_id integer [pk]
  order_id integer
  product_id integer
  quantity integer
}

Table products {
  product_id integer [pk]
  product_name varchar(255)
  category_id integer
  unit varchar(255)
  price decimal(10,2)
}

Table testproducts {
  testproduct_id integer [pk]
  product_name varchar(255)
  category_id integer
}

// Relationships
Ref: customers.customer_id < orders.customer_id
Ref: orders.order_id < order_details.order_id
Ref: products.product_id < order_details.product_id
Ref: categories.category_id < products.category_id