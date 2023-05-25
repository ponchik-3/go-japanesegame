go-game: main.o constructors.o output_operators.o dot_operators.o dot_acceptance.o putdot.o conn_check.o player_opers.o are_conns_posbl.o get_acc_neighb.o
	g++ main.o constructors.o output_operators.o dot_operators.o dot_acceptance.o putdot.o conn_check.o player_opers.o are_conns_posbl.o get_acc_neighb.o -o go-game


constructors.o: constructors.cpp
	g++ -c constructors.cpp

output_operators.o: output_operators.cpp
	g++ -c output_operators.cpp

dot_operators.o: dot_operators.cpp
	g++ -c dot_operators.cpp

dot_acceptance.o: dot_acceptance.cpp
	g++ -c dot_acceptance.cpp

putdot.o: putdot.cpp
	g++ -c putdot.cpp

conn_check.o: conn_check.cpp
	g++ -c conn_check.cpp

player_opers.o: player_opers.cpp
	g++ -c player_opers.cpp

main.o: main.cpp
	g++ -c main.cpp

are_conns_posbl.o: are_conns_posbl.cpp
	g++ -c are_conns_posbl.cpp

get_acc_neighb.o: get_acc_neighb.cpp
	g++ -c get_acc_neighb.cpp

clean:
	rm *.o go-game