from django.apps import AppConfig
import os
import logging

class ChatbotConfig(AppConfig):
    name = 'chatbot'

    def ready(self):
        template_dir = os.path.join(os.path.dirname(__file__), 'templatetags')
        if os.path.exists(template_dir):
            logging.info(f"Template directory exists: {template_dir}")
        else:
            logging.error(f"Template directory does not exist: {template_dir}")
