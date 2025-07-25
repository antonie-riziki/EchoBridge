import streamlit as st 
from code_editor import code_editor

st.title("Getting started")

st.subheader("Prerequisite")

st.markdown("""

    Before we begin, make sure you have the following:

    \n- An Africa’s Talking account

    \n- A registered sender ID (optional, but ideal for production)

    \n- Username & API key 

""")

st.subheader("Installation")



# Python installation 
st.write('- **Python**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies (pip)
    pip install africastalking python-dotenv
    """, language="python")

st.write('Copy to your Script')
st.code("""
    import africastalking
    import os
    from dotenv import load_dotenv

    load_dotenv()

    africastalking.initialize(
        username='YOUR_USERNAME',
        api_key = os.getenv("AT_API_KEY")
    )

""", language="python")
# code_editor('pip install africastalking python-dotenv', lang='python')



# Noje.js & JavaScript installation 
st.write('- **Node.js / JavaScript**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies (npm)
    npm install africastalking
    """, language="javascript")

st.write('Copy to your Script')
st.code("""
    const AfricasTalking = require('africastalking')({
        apiKey: process.env.AT_API_KEY,
        username: process.env.AT_USERNAME
    });
""", language="javascript")
# code_editor('pip install africastalking python-dotenv', lang='python')




# Ruby installation 
st.write('- **Ruby**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies 
    gem 'africastalking'
    """, language="ruby")

st.write('Copy to your Script')
st.code("""
    require "AfricasTalking"

    username = "USERNAME"      
    api_key  = "YOUR_API_KEY" 

    at = AfricasTalking::Initialize.new(username, api_key)

""", language="ruby")
# code_editor('pip install africastalking python-dotenv', lang='python')



# Typscript installation 
st.write('- **Typescript**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies (npm)
    npm install africastalking
    npm install --save-dev @types/africastalking
    """, language="typescript")

st.write('Copy to your Script')
st.code("""
    import AfricasTalking from "africastalking";

    const africastalking = AfricasTalking({
        username: "USERNAME",            
        apiKey: "YOUR_API_KEY",        
    });

""", language="typescript")
# code_editor('pip install africastalking python-dotenv', lang='python')




# Rust installation 
st.write('- **Rust**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies
    cargo install --git https://github.com/rust-nairobi/africastalking-rust
    """, language="rust")

st.write('Copy to your Script')
st.code("""
    use africastalking_gateway::AfricasTalkingGateway;

    fn main() {
        let username = "USERNAME";      
        let apikey = "YOUR_API_KEY";   
        let env = "USERNAME";           

        let gateway = AfricasTalkingGateway::new(&username, &apikey, &env);
""", language="rust")
# code_editor('pip install africastalking python-dotenv', lang='python')




# Kotlin installation 
st.write('- **Kotlin**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies
    repositories {
        maven("https://jitpack.io")
        }

        dependencies {
            implementation("com.github.AfricasTalkingLtd.africastalking-java:core:3.4.11")
        }

    """, language="kotlin")

st.write('Copy to your Script')
st.code("""
    import com.africastalking.AfricasTalking

    fun main() {
        val username = "USERNAME"      
        val apiKey   = "YOUR_API_KEY" 

        AfricasTalking.initialize(username, apiKey)
    }
""", language="kotlin")
# code_editor('pip install africastalking python-dotenv', lang='python')




# PHP installation 
st.write('- **PHP**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies
    composer require africastalking/africastalking
    """, language="php")

st.write('Copy to your Script')
st.code("""
    <?php
    require 'vendor/autoload.php';

    use AfricasTalking\SDK\AfricasTalking;

    $username = 'USERNAME';      
    $apiKey   = 'YOUR_API_KEY'; 

    $AT = new AfricasTalking($username, $apiKey);
""", language="php")
# code_editor('pip install africastalking python-dotenv', lang='python')




# Java installation 
st.write('- **Java**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies
    repositories {
        maven { url "https://jitpack.io" }
        }

        dependencies {
        implementation 'com.github.AfricasTalkingLtd.africastalking-java:core:3.4.11'
        }

    """, language="java")

st.write('Copy to your Script')
st.code("""
    import com.africastalking.AfricasTalking;
    import com.africastalking.SmsService;

    public class Main {
        public static void main(String[] args) {
            String username = "USERNAME";     
            String apiKey = "YOUR_API_KEY";  
            
            // Initialize the SDK
            AfricasTalking.initialize(username, apiKey);

            }
        }
""", language="java")
# code_editor('pip install africastalking python-dotenv', lang='python')