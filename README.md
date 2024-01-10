# luwa

To create photorealistic lighting, you must correctly configure each lamp in the scene. Blender's default unit of measurement for adjusting lamp power is watts. This is enough in most cases, but it can also cause some inconsistencies when colors vary.

For example, a yellow bulb will illuminate a room much more efficiently than a blue bulb of the same power. A bulb of the same power in white will illuminate better than both. This occurs because the human eye does not have the same sensitivity for all frequencies in the visible spectrum.

For this reason, architects and archviz artists often use lumens, a more appropriate unit of measurement to describe the luminous flux perceived by the human eye. This value is informed by the lamp manufacturers, but to use it in Blender you need to convert it into watts.

The LuWa script matches the manufacturer-specified lumen value with the lamp color and returns the appropriate wattage for a more accurate lighting study. Thus, if the yellow, blue and white bulbs have the same lumen value, they will illuminate equally, but the watts of the blue bulb will be the highest, followed by the yellow one and, finally, the white one, the most efficient.
