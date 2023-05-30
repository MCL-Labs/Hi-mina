INSERT INTO api_keys (key, current_tokens) VALUES ('my_api_key', 100);
UPDATE api_keys SET current_tokens = 50 WHERE key = 'my_api_key';
DELETE FROM api_keys WHERE key = 'my_api_key';