// [config]
// expect_result: fail
// glsl_version: 4.20
//
// [end config]

/* FAIL */
#version 420
struct s1 { float f; };

struct s2 { s1 f; };

void main()
{
    s1 t = { { 1 } };
}