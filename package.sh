#https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/

mkdir pkg

cp src/*.py pkg

cd pkg

pip install boto3 -t ./

chmod -R 755 .

zip -r ubiqTempLambda.zip .

mv ubiqTempLambda.zip ..

