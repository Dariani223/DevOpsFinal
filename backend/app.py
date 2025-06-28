from flask import Flask, jsonify, send_from_directory, request
from prometheus_client import Counter, Histogram, Gauge, generate_latest
import time
import os
import psutil
import os  # Already imported but ensure it's used for secrets
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total app requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('app_request_duration_seconds', 'Request duration')
ACTIVE_CONNECTIONS = Gauge('app_active_connections', 'Active connections')
CPU_USAGE = Gauge('app_cpu_usage_percent', 'CPU usage percentage')
MEMORY_USAGE = Gauge('app_memory_usage_bytes', 'Memory usage in bytes')

# App state
start_time = time.time()
request_count = 0

@app.before_request
def before_request():
    global request_count
    request_count += 1
    REQUEST_COUNT.labels(method=request.method, endpoint=request.endpoint).inc()

@app.route('/')
def index():
    """Serve the frontend"""
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Backend service is running',
        'uptime': time.time() - start_time,
        'timestamp': time.time()
    })

@app.route('/api/metrics')
def metrics_endpoint():
    """Application metrics endpoint"""
    # Update system metrics
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().used)
    ACTIVE_CONNECTIONS.set(request_count % 100)  # Simulated active connections
    
    return jsonify({
        'requests': request_count,
        'uptime': time.time() - start_time,
        'cpu_percent': psutil.cpu_percent(),
        'memory_mb': psutil.virtual_memory().used / 1024 / 1024,
        'status': 'healthy'
    })

#@app.route('/metrics')
# def prometheus_metrics():
#     """Prometheus metrics endpoint"""
#     # Update metrics before serving
#     CPU_USAGE.set(psutil.cpu_percent())
#     MEMORY_USAGE.set(psutil.virtual_memory().used)
#     ACTIVE_CONNECTIONS.set(request_count % 100)
    
#     return generate_latest()
@app.route('/metrics')
def metrics():
    # Update metrics
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().used)
    return generate_latest()


@app.route('/api/load')
def generate_load():
    """Generate CPU load for testing"""
    start = time.time()
    # Simulate work for 1 second
    while time.time() - start < 1:
        _ = sum(i * i for i in range(1000))
    
    return jsonify({
        'message': 'Load generated successfully',
        'duration': time.time() - start
    })

@app.route('/api/error')
def simulate_error():
    """Simulate an error for testing"""
    return jsonify({'error': 'Simulated error'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print(f"Starting backend service...")
    print(f"Health check: http://localhost:5000/api/health")
    print(f"Metrics: http://localhost:5000/metrics")
    app.run(host='0.0.0.0', port=5000, debug=True)