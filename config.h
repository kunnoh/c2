#include <iostream>

static unsigned char CONFIG_BUFFER[2000] = "{\"Hostname\":\"Please\", \"Migrate\":\"Subscribe\"}";

struct config_t{
    std::string Hostname;
    std::string Migrate;
};
typedef struct config_t CONFIG;
void config_initialize(struct config_t *Config, std::string ConfigStr);