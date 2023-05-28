go-game: main.o constructors.o output_operators.o dot_operators.o dot_acceptance.o putdot.o conn_check.o player_opers.o are_conns_posbl.o get_acc_neighb.o dot_pos.o conn_posiblt.o find_conns.o make_conns.o get_area.o wave_area.o get_place.o choose_dot.o
	g++ main.o constructors.o output_operators.o dot_operators.o dot_acceptance.o putdot.o conn_check.o player_opers.o are_conns_posbl.o get_acc_neighb.o dot_pos.o conn_posiblt.o find_conns.o make_conns.o get_area.o wave_area.o get_place.o choose_dot.o -o go-game


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

dot_pos.o: dot_pos.cpp
	g++ -c dot_pos.cpp

conn_posiblt.o: conn_posiblt.cpp
	g++ -c conn_posiblt.cpp

find_conns.o: find_conns.cpp
	g++ -c find_conns.cpp

make_conns.o: make_conns.cpp
	g++ -c make_conns.cpp

get_area.o: get_area.cpp
	g++ -c get_area.cpp

wave_area.o: wave_area.cpp
	g++ -c wave_area.cpp

get_place.o: get_place.cpp
	g++ -c get_place.cpp

choose_dot.o: choose_dot.cpp
	g++ -c choose_dot.cpp


clean:
	rm *.o go-game