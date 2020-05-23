#!/usr/bin/python -tt

import sys

def qualify_bet(inputs):
  """Calculate a matched qualifying bet"""
  print 'Qualifying bet:'
  back_value = inputs['bet_value']
  back_odds = inputs['bet_odds']
  lay_odds = inputs['lay_odds']
  commission_per_cent = inputs['commission_per_cent']
  # With inputs in place calculate bet
  commission = 0.01 * commission_per_cent
  lay_stake = (back_value * back_odds) / (lay_odds - commission)
  # Calculate profit in both cases (back wins and back loses)
  profit_back_wins = back_value * (back_odds - 1) \
  - lay_stake * (lay_odds - 1)
  profit_lay_wins = lay_stake * (1 - commission) - back_value
  # Print calculated outputs
  print 'Profit if *back* wins: GBP', round(profit_back_wins,2)
  print 'Profit if *lay* wins: GBP', round(profit_lay_wins,2)  
  print 'Lay required: GBP', round(lay_stake,2)

def free_bet(inputs):
  """Calculate a matched free bet"""
  print 'Free bet:'
  free_value = inputs['bet_value']
  free_odds = inputs['bet_odds']
  lay_odds = inputs['lay_odds']
  commission_per_cent = inputs['commission_per_cent']
  # With inputs in place calculate bet
  commission = 0.01 * commission_per_cent
  lay_stake = free_value * (free_odds - 1) / (lay_odds - commission)
  # Calculate profit in both cases (free back wins and free back loses)
  profit_free_wins = free_value * (free_odds - 1) \
  - lay_stake * (lay_odds - 1)
  profit_lay_wins = lay_stake * (1 - commission)
  # Also calculate free SNR value
  free_SNR = profit_free_wins / free_value
  free_SNR_per_cent = free_SNR * 100
  # Print calculated outputs
  print 'Profit if *back* wins: GBP', round(profit_free_wins,2)
  print 'Profit if *lay* wins: GBP', round(profit_lay_wins,2) 
  print 'Free value %: ', round(free_SNR_per_cent,1), '%'
  print 'Lay required: GBP', round(lay_stake,2)


def request_input(type):
  """ Get user input of bet values. Returns dict of mapped values. """
  inputs = {}
  if type == '-qual' or type == '-q' \
  or type == '-free' or type == '-f':
    inputs['bet_value'] = float(raw_input('Enter bet value:\n'))
    inputs['bet_odds'] = float(raw_input('Enter bet decimal odds\n'))
    inputs['lay_odds'] = float(raw_input('Enter lay decimal odds\n'))
    inputs['commission_per_cent'] = float(raw_input('Enter exchange commission in %\n'))
  return inputs
  


def main():

  args = sys.argv[1:]
  # If no system arguments provided, ask what type of bet
  if not args:
    args = []
    print 'What type of bet?'
    print "'q' = qualifying bet'"
    print "'f' = free bet"
    # Add other options
    args.append('-' + raw_input('Enter bet type:\n'))
  # Then use the first input as bet type
  bet_type = args[0]
  # If only one argument provided get bet parameter inputs
  if len(args) == 1:
    print 'Bet inputs not provided, requesting inputs'
    inputs = request_input(bet_type)
  # If system arguments provided bet parameters build the input dict     
  elif len(args) >= 4:
    inputs = {}
    inputs['bet_value'] = float(args[1])
    inputs['bet_odds'] = float(args[2])
    inputs['lay_odds'] = float(args[3])
    # If only three bet parameters assume 0% commission
    if len(args) == 4:
      print 'Commission not provided - assuming 0% commission'
      inputs['commission_per_cent'] = 0.0
    # Otherwise take the final parameter as commission  
    else:  
      inputs['commission_per_cent'] = float(args[4])
  # For other argument lengths exit with an error    
  else:
    print 'Unknown inputs given, exit and try again'
    sys.exit[1]
    
  # Check bet type and call appropriate function  
  if bet_type == '-q' or bet_type =='-qual':
    qualify_bet(inputs)
  elif bet_type == '-f' or bet_type == '-free':
    free_bet(inputs)
  else:
    print "Bet type not recongised. Use 'q' for qualifying or 'f' for free."
      
  
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
