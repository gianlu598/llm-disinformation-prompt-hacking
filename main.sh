#! /bin/bash

# setup
if ! test -d openai-env ; then
  #download and install virtualenv library
  apt-get install -y python3-venv
  #create virtual environment
  python3 -m venv openai-env
  #activate virtual environment
  source openai-env/bin/activate
  #install required libraries
  pip3 install -r requirements.txt
else
  #virtual env already exists.. activate virtual environment
  source openai-env/bin/activate
fi

#test permissions
if ! test -x python/main.py ; then
  chmod u+x python/main.py
fi

#ask for the OPENAI_API_KEY
if [ -z "${OPENAI_API_KEY}" ]; then
  read -p "OPENAI API KEY: " openai_api_key
  export OPENAI_API_KEY=$openai_api_key
else
  echo $OPENAI_API_KEY
fi

#text art
cat assets/title-ascii-text-art.txt

#execute the program
python python/main.py

#deactivate virtual environment
deactivate
