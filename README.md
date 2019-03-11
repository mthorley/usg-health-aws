# usg-health-aws
Lambda invocation of Unifi APIs to verify health including temperatures

 * Invokes device API on Unifi controller to get USG and USW information and outputs stats (currently temperatures) to Cloudwatch.
 * Uses a read-only account on controller. Credentials are captured from Lambda environment encrypted by KMS.
 * Cloudwatch rule schedules lambda execution every 5 minutes.
