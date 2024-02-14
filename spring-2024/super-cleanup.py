from hub import port
import runloop
import motor
import force_sensor

async def main():
    while True:
        # Wait for the force sensor to be pressed
        await runloop.until(lambda: force_sensor.pressed(port.E))
        motor.run(port.A,-750)
        # Wait for the force sensor to be released
        await runloop.until(lambda: not force_sensor.pressed(port.E))
        motor.run(port.A, 750)

runloop.run(main())
