from key2cursor.config_manager import ConfigManager

def main():
    config_manager = ConfigManager()

    config_manager.save_mouse_mode("j")

if __name__ == "__main__":
    # python -m test.test_json_save
    main()