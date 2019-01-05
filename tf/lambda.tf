

/*
FIXME: Create this role rather than source it
*/
data "aws_iam_role" "lambda_exec_role" {
  name = "CMLambdaExecutionRole"
}

resource "aws_lambda_function" "unifi_temp_lambda" {
  filename         = "../ubiqTempLambda.zip"
  function_name    = "ubiquiti_temp"
  role             = "lambda_exec_role"
  handler          = "lambda_handler"
  source_code_hash = "${base64sha256(file("../ubiqTempLambda.zip"))}"
  runtime          = "python2.7"

  environment {
    variables = {
      foo = "bar"
    }
  }
}


