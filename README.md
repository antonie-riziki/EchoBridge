# EchoBridge

EchoBridge is a developer-friendly, sandboxed integration platform for Africa’s Talking services. It allows you to plug in your Africa’s Talking credentials (API key and username) and immediately start building and testing SMS, USSD, voice, airtime, and payment services. You can begin in sandbox mode, which uses Africa’s Talking’s sandbox username and test key, to simulate your workflows and then seamlessly switch to live mode when you’re ready for production.

As a microservices orchestration hub, EchoBridge is designed for growth. After integrating with Africa’s Talking, you can easily plug in additional APIs, such as cloud functions, AI endpoints, mapping services, or IoT devices, without overhauling your core setup.

## Features

*   **Sandbox Environment:** Test your Africa's Talking integrations in a secure sandbox environment without incurring charges.
*   **Seamless Transition to Live Mode:** Easily switch from sandbox to live mode when you're ready to go into production.
*   **Support for Multiple Services:** EchoBridge supports a wide range of Africa's Talking services, including:
    *   SMS
    *   USSD
    *   Voice
    *   Airtime
    *   Payments
*   **Extensible Architecture:** The modular design of EchoBridge allows you to easily integrate additional microservices and APIs.
*   **User-Friendly Interface:** The application provides a clean and intuitive interface for managing your integrations.

## Getting Started

### Prerequisites

*   Python 3.7+
*   An Africa's Talking account. If you don't have one, you can sign up at [africastalking.com](https://africastalking.com/).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/antonie-riziki/EchoBridge.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage

Once the application is running, you can use the sidebar to navigate between the different pages:

*   **Register:** Create a new account.
*   **Sign In:** Log in to your existing account.
*   **Home Page:** View an overview of the application and its features.
*   **Getting Started:** Follow a step-by-step guide to set up your Africa's Talking account and obtain your API credentials.
*   **Setup & Installation:** Configure your Africa's Talking credentials and other settings.
*   **Messaging:** Send and receive SMS messages, and manage your USSD menus.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with a descriptive commit message.
4.  Push your changes to your forked repository.
5.  Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
