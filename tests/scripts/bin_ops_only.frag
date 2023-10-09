const float PI = 3.14159;

in float t;
in float phase, frequency, amplitude;
out float value, value2;

void main()
{
    value = amplitude * (t+phase) * 2*PI/frequency;
    value2 = 42;
}