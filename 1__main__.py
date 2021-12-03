import pulumi
import pulumi_aws as aws

#=================CReate S3 for logs=================


logs_bucket = aws.s3.Bucket('requestLogs', bucket="myawslogbucket.s3.amazonaws.com" , acl='log-delivery-write')

#====================================================
#==================S3 bucket for web ================
bucket = aws.s3.Bucket("bucket",
    acl="private",
    tags={
        "Name": "My bucket",
    })
s3_origin_id = "myS3Origin"
s3_distribution = aws.cloudfront.Distribution("s3Distribution",
    origins=[aws.cloudfront.DistributionOriginArgs(
        domain_name=bucket.bucket_regional_domain_name,
        origin_id=s3_origin_id,
        s3_origin_config=aws.cloudfront.DistributionOriginS3OriginConfigArgs(
            origin_access_identity="origin-access-identity/cloudfront/E2APONMGZPZRLL",
        ),
    )],
    enabled=True,
    is_ipv6_enabled=True,
    comment="Some comment",
    default_root_object="index.html",

#============Logs to bucket for Logs============

    logging_config=aws.cloudfront.DistributionLoggingConfigArgs(
        include_cookies=False,
        bucket="myawslogbucket.s3.amazonaws.com" ,
        prefix="log/",
    ),
    default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
        allowed_methods=[
            "GET",
            "HEAD"
        ],
        cached_methods=[
            "GET",
            "HEAD",
        ],
        target_origin_id=s3_origin_id,
        forwarded_values=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs(
            query_string=False,
            cookies=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs(
                forward="none",
            ),
        ),
        viewer_protocol_policy="allow-all",
        min_ttl=0,
        default_ttl=3600,
        max_ttl=86400,
    ),
    ordered_cache_behaviors=[
        aws.cloudfront.DistributionOrderedCacheBehaviorArgs(
            path_pattern="/content/immutable/*",
            allowed_methods=[
                "GET",
                "HEAD",
            ],
            cached_methods=[
                "GET",
                "HEAD",
            ],
            target_origin_id=s3_origin_id,
            forwarded_values=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesArgs(
                query_string=False,
                headers=["Origin"],
                cookies=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs(
                    forward="none",
                ),
            ),
            min_ttl=0,
            default_ttl=86400,
            max_ttl=31536000,
            compress=True,
            viewer_protocol_policy="redirect-to-https",
        ),
        aws.cloudfront.DistributionOrderedCacheBehaviorArgs(
            path_pattern="/content/*",
            allowed_methods=[
                "GET",
                "HEAD",
            ],
            cached_methods=[
                "GET",
                "HEAD"
            ],
            target_origin_id=s3_origin_id,
            forwarded_values=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesArgs(
                query_string=False,
                cookies=aws.cloudfront.DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs(
                    forward="none",
                ),
            ),
            min_ttl=0,
            default_ttl=3600,
            max_ttl=86400,
            compress=True,
            viewer_protocol_policy="redirect-to-https",
        ),
    ],
    price_class="PriceClass_200",
    restrictions=aws.cloudfront.DistributionRestrictionsArgs(
        geo_restriction=aws.cloudfront.DistributionRestrictionsGeoRestrictionArgs(
            restriction_type="whitelist",
            locations=[
                "US",
                "CA",
                "GB",
                "DE",
            ],
        ),
    ),
    tags={
        "Environment": "production",
    },
    viewer_certificate=aws.cloudfront.DistributionViewerCertificateArgs(
        cloudfront_default_certificate=True,
    ))
