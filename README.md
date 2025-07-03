# vcgencmd-exporter

A lightweight Prometheus exporter for Raspberry Pi, exposing temperature and throttling metrics using `vcgencmd`.

## Features

- Reports CPU temperature in Celsius and Fahrenheit
- Reports throttling status from `vcgencmd get_throttled`
- Isolates current throttling conditions to avoid false positives (`rpi_throttled_current`)
- Designed for use with Prometheus + Grafana

## Metrics Exposed

| Metric                    | Description                                |
|---------------------------|--------------------------------------------|
| `rpi_temp`                | CPU temperature in Celsius                 |
| `rpi_temp_f`              | CPU temperature in Fahrenheit              |
| `rpi_throttled_status`    | Full bitmask from `vcgencmd get_throttled` |
| `rpi_throttled_current`   | Bits 0–2 only (current active throttling)  |

## Example

```bash
curl http://<raspberry-pi>:9101/
