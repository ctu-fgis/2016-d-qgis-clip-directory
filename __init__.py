# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ClipDirectoryPlugin
                                 A QGIS plugin
 This plugin is used to clip all shapefiles contained in the selected directory.
                             -------------------
        begin                : 2016-06-19
        copyright            : (C) 2016 by Jan Zacharias
        email                : jan.zacharias@seznam.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ClipDirectoryPlugin class from file ClipDirectoryPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .clipdirectoryplugin import ClipDirectoryPlugin
    return ClipDirectoryPlugin(iface)
