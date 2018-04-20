from projectBase import ProjectBase
import os



class Reels(object):

    def __init__(self, testCase):
        # type: (ProjectBase) -> None
        """
        :param testCase: will be the ProjectBase object when a test is run.
        """
        self.testCase = testCase

    def getReelsTab(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH, '//div[text()="Reels"]')
        el = self.testCase.UIType.Element(el)
        return el

    def tapCircuitsOnReel(self):
        el = self.getReelsTab()
        el.tap()

    def switchToReelsTab(self):
        el = self.getReelsTab()
        if el.ui_object.get_attribute('class') != 'selected':
            el.tap()

    def getReelsEmptyState(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'p.important-message')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    # get the reels table info
    def getReelName(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        reelName = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.header-left')
        reelName = self.testCase.UIType.Element(reelName)
        return reelName.getLabel()

    def getReelPackage(self):
        # get the selected reel container
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR,
                                                  'div.selected.reel-list-item-container')
        package = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.package-name')
        package = self.testCase.UIType.Element(package)
        return package.getLabel()

    def getReelSize(self):
        # get reel size info
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH,
                                           '//div[contains(text(), "Reel Size")]')
        # get numeric size
        size = el.text
        number = size.split(' ')[-1]
        number = self.testCase.UIType.Element(number)
        return number

    def getReelWeight(self):
        # get reel weight info
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().XPATH,
                                           '//div[contains(text(), "Reel Weight")]')
        # get numeric size
        weight = el.text
        number = weight.split(' ')[-1]
        number = self.testCase.UIType.Element(number)
        return number

    def tapExpandArrow(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.expand.down')
        el = self.testCase.UIType.Button(el)
        el.tap()

    # get circuit on reel info
    def getACircuitOnReel(self, rowOrder):
        # get table
        table = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'tbody')
        # get the list of rows from the table
        rows = table.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'tr')

        selectedRow = rows[rowOrder]
        return selectedRow

    def getCircuitFromOnReel(self, rowOrder=0):
        row = self.getACircuitOnReel(rowOrder)
        circuitFrom = row.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'td.from-cell')
        circuitFrom = self.testCase.UIType.Element(circuitFrom)
        return circuitFrom.getLabel()

    def getCircuitToOnReel(self, rowOrder=0):
        row = self.getACircuitOnReel(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitTo = allTds[1]
        circuitTo = self.testCase.UIType.Element(circuitTo)
        return circuitTo.getLabel()

    def getCircuitSizeOnReel(self, rowOrder=0):
        row = self.getACircuitOnReel(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitSize = allTds[2]
        circuitSize = self.testCase.UIType.Element(circuitSize)
        return circuitSize.getLabel()

    def getCircuitLengthOnReel(self, rowOrder=0):
        row = self.getACircuitOnReel(rowOrder)
        allTds = row.find_elements(self.testCase.app.getStrategy().CSS_SELECTOR, 'td')
        circuitLength = allTds[3]
        circuitLength = self.testCase.UIType.Element(circuitLength)
        return circuitLength.getLabel()

    def getCircuitMetal(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.expanded-header')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'span')
        text = el.text
        metal = text.split(' ')[3]
        metal = self.testCase.UIType.Element(metal)
        return metal

    def getCircuitInsulation(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.expanded-header')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'span')
        text = el.text
        insulation = text.split(' ')[5]
        insulation = self.testCase.UIType.Element(insulation)
        return insulation

    def getCircuitColor(self):
        container = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.selected-color')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'div.color-label')
        el = self.testCase.UIType.Element(el)
        return el.getLabel()

    def getCircuitToggle(self):
        container = self.testCase.app.findElements(self.app.getStrategy().CSS_SELECTOR, 'div.checkbox-toggle')
        el = container.find_element(self.testCase.app.getStrategy().CSS_SELECTOR, 'input')
        el = self.testCase.UIType.Element(el)
        return el

    def getBullseyeVisualization(self):
        el = self.testCase.app.findElement(self.testCase.app.getStrategy().CSS_SELECTOR, 'svg.reel-bullseye')
        el = self.testCase.UIType.Element(el)
        return el 
