import fileinput
from datetime import datetime, timedelta

class TradeReconcilation:
    # we create a dictionary of list of records
    # records are <key,value> pair where key -> exchangeName and value is list of records like ->
    # (product,qty,timestamp)
    # thus we will have for example
    # { 'AKUMA': [(A,20,10:30:00),(B,-15,10:05:00)] .. etc
    record_hist = {}

    def process(self, line: str) -> str:
        # after splitting the list by ,
        # we get the trade name here and remaining elements are stored in form of a list called elements
        source, *elements = line.split(',')

        # if trade name is not RECONCILIATION we will just store the trade in the respective
        # then we just record a new trade
        if source != 'RECONCILIATION':
            # we get product, quantity and timestamp from unpacking the list
            product, quantity, timestamp = elements
            # new trade
            if source not in self.record_hist.keys():
                # create a list and populate it with trade elements
                self.record_hist[source] = [(product, quantity, timestamp)]
            else:
                # add trade elements to the existing trade
                self.record_hist[source].append((product, quantity, timestamp))
            return quantity  # return the quantity which is a str as of now
        else:
            # for reconciliation

            # here we will go through the trades involving first source and check if these trades are present in the
            # trade list of counterpart.
            # if the trade list is not there we add it to a filtered list
            # we return the length of the filtered list which basically has trade elements present in first source but
            # not in counterpart
            first_source = elements[0]
            counterpart = elements[1]

            # if first source has no trade elements return 0
            if first_source not in self.record_hist.keys():
                return "0"
            # if counter part has no trade elements then just return the count of total trade elements in first source
            elif counterpart not in self.record_hist.keys():
                return str(len(self.record_hist[first_source]))
            else:
                # create a filtered list having trade elements in first source but not in counter part
                filtered_trade_list = list(
                    filter(lambda x: x not in self.record_hist[counterpart], self.record_hist[first_source]))
                # return the string form of length of the trade list that has count of such trade elements
                return str(len(filtered_trade_list))

    def reconciliation(self) -> bool:
        # generally reconciliation will happen between AKUNA and EXCHANGE

        # since it is one-to-one exchange thus total trades for akuna and exchange must be same
        if len(self.record_hist['AKUNA']) != len(self.record_hist['EXCHANGE']):
            return False
        # if the exchange that has been successfully mapped with an akuna trade is not being considered
        # since it is added to this set
        exchange_visited_set = set()
        # we unpack the values
        for akuna_product, akuna_qty, akuna_timestamp in self.record_hist['AKUNA']:

            found_reconciliation = False # to check if reconciliation if found for current iteration

            for exchange_product, exchange_qty, exchange_timestamp in self.record_hist['EXCHANGE']:

                # we convert the string to time
                akuna_time = datetime.strptime(akuna_timestamp, '%H:%M:%S')
                exchange_time = datetime.strptime(exchange_timestamp, '%H:%M:%S')

                # if the current trade is not in the set then it means it has not been reconciled yet
                if (exchange_product, exchange_qty, exchange_timestamp) not in exchange_visited_set:
                    # check for reconciliation
                    if akuna_product == exchange_product and akuna_qty == exchange_qty and \
                            abs(akuna_time-exchange_time) <= timedelta(minutes=5):
                        # if true, we set reconciliation to true
                        found_reconciliation = True
                        # we add the exchange trade to the set so that it is not taken into consideration for future
                        # akuna trades
                        exchange_visited_set.add((exchange_product, exchange_qty, exchange_timestamp))
                        break
            # in this case there was an akuna trade which did not reconciliate with exchange trade so we return false
            if not found_reconciliation:
                return False
        # if all is done then return true
        return True



# driver code
if __name__ == '__main__':
    rec_engine = TradeReconcilation()
    # file name given here
    for line in fileinput.input('./input.txt'):
        cleaned_line = line.replace("\n", "")
        rec_engine.process(cleaned_line)
    print(rec_engine.reconciliation())
