#https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/

mkdir pkg

cd pkg

rm -rf *

cp ../src/*.py .

# boto3 already provided by lambda
pip install requests -t ./

chmod -R 755 .

zip -r ubiqTempLambda.zip .

mv ubiqTempLambda.zip ..

