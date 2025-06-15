#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>


__global__ void saxpy(int n, float a, float *x, float *y) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n)
        y[i] = a * x[i] + y[i];
}

void benchmark_saxpy(int n) {
    float *x, *y, *d_x, *d_y;
    float a = 2.0f;

    size_t size = n * sizeof(float);
    x = (float*)malloc(size);
    y = (float*)malloc(size);

    for (int i = 0; i < n; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    cudaMalloc(&d_x, size);
    cudaMalloc(&d_y, size);

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    cudaMemcpy(d_x, x, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_y, y, size, cudaMemcpyHostToDevice);

    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    cudaEventRecord(start);
    saxpy<<<blocksPerGrid, threadsPerBlock>>>(n, a, d_x, d_y);
    cudaEventRecord(stop);

    cudaEventSynchronize(stop);
    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);

    printf("N = %8d | Time = %8.4f ms\n", n, milliseconds);

    cudaFree(d_x);
    cudaFree(d_y);
    free(x);
    free(y);
}

int main() {
    printf("SAXPY Benchmark (GPU only kernel time)\n");
    for (int exp = 15; exp <= 25; exp++) {
        int n = 1 << exp;
        benchmark_saxpy(n);
    }
    return 0;
}
