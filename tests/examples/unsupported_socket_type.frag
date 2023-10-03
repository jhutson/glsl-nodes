const float PI = 3.14159;

in float t;
in float phase, frequency, amplitude;
out int value;

void main()
{
    value = amplitude * sin((t+phase) * 2*PI/frequency);
}