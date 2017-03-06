namespace py lambda_thrift_service

service MultiplicationService
{
    i32 multiply(1:i32 n1, 2:i32 n2),
}
