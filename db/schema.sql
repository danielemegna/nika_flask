DROP TABLE IF EXISTS listings;

CREATE TABLE listings(
  property_transaction_id TEXT NOT NULL,
  address_street TEXT NULL,
  address_street_number TEXT NULL,
  address_city TEXT NULL,
  address_zip_code TEXT NULL,
  is_candidate BOOL NOT NULL
);
